import discord
import os
from dotenv import load_dotenv
from discord.ext import commands,tasks
from scrape import PlanScraperForApocryph
import asyncio

load_dotenv()

bot = commands.Bot(command_prefix='|', description='First iteration of Apocryph')

# Custom class for scraping data from the university site
plan_scraper = PlanScraperForApocryph()

@bot.event
async def on_ready():
    """
    When bot loggs in on the server it displays its name and id,
    also setting his status as watching Activity
    :return: None
    """
    print("I'm ready!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="students suffer"))


@bot.command()
async def plan_zajec(ctx):
    """
    :param ctx: context
    Displays study classes in a channel
    :return Plan in JPG form
    """
    plan_scraper.get_plan()
    await ctx.send(file=discord.File(fp='Plans/PlanJPGS/plan.jpg'))

@bot.command()
async def plany(ctx):
    """
    :param new: Display only new plans
    :param ctx: context
    Displays newly changed plans
    Do poprawy w najbliższym czasie !!! Duplikacja kodu
    :return:
    """
    plans = plan_scraper.fresh_plans(False)
    # Jeżeli wyświetlamy wszystkie plany
    embed_list = discord.Embed(
        title="Plany zajęć",
        colour=discord.Colour.blue()
    )
    if len(plans) != 0:
        for plan in plans:
            embed_list.add_field(name=plan['semestr'], value=plan['link'], inline=False)
        await ctx.send(embed=embed_list)
    else:
        embed_list = discord.Embed(
            title="Plany zajęć",
            colour=discord.Colour.blue()
        )
        embed_list.set_image(url='https://www.weeren.net/nothing.gif')
        await ctx.send(embed=embed_list)


@tasks.loop(seconds=10)
async def new_plans_checker(ctx):
    await ctx.send("Iteration Done")

@bot.command()
async def dz(ctx, *args):
    await ctx.send(f'**Dodano zadanie** {args[0]}\n'
                   f'**Cel:** {args[1]}')
    try:
        quests = open('etc/quests.txt', 'a')
    except FileNotFoundError:
        quests = open('etc/quests.txt', 'w')
    for item in args:
        quests.write(f'{item} ')
    quests.write('\n')


@bot.command()
async def wz(ctx):
    try:
        quest_file = open('etc/quests.txt', 'r')
        quest_list = quest_file.readlines()
        embed_list = discord.Embed(
            title="Quest List",
            colour=discord.Colour.blue()
        )

        for line in quest_list:
            splittedline = line.split(" ")
            embed_list.add_field(name=splittedline[0],
                                 value=' '.join(splittedline[1:len(splittedline) - 1]), inline=False)
        await ctx.send(embed=embed_list)
    except FileNotFoundError:
        await ctx.send('Brak zadań na liście :)')


@bot.command()
async def uz(ctx, indx):
    quest_file_read = open('etc/quests.txt', 'r')
    lines = []

    if indx == 'all':
        quest_file_read.close()
        os.remove('etc/quests.txt')
        await ctx.send('Usunieto wszystkie zadania!!!')
    else:
        for i, line in enumerate(quest_file_read):
            if i != int(indx) - 1:
                lines.append(line)
            elif i == int(indx) - 1:
                deleted_task = line

        splitted_line = deleted_task.split(" ")
        cel = ' '.join(splitted_line[1:len(splitted_line) - 1])
        quest_file_write = open('etc/quests.txt', 'w')
        quest_file_write.writelines(lines)
        await ctx.send(f'**Usunieto zadanie** {splitted_line[0]}\n'
                       f'**Cel:** {cel}')

bot.run(os.getenv('XENO_TOKEN'))

# discord.py
# requests
# wget
# python-dotenv
# beautifulsoup4
# pdf2image

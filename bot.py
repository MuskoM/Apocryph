import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from scrape import PlanScraperForApocryph

load_dotenv()

bot = commands.Bot(command_prefix='^', description='First iteration of Apocryph')

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
async def plany(ctx, new=False):
    """
    :param new: Display only new plans
    :param ctx: context
    Displays newly changed plans
    Do poprawy w najbliższym czasie !!! Duplikacja kodu
    :return:
    """
    new_plans = plan_scraper.fresh_plans(new)
    # Jeżeli trzeba wyświetlić nowe plany
    if new:
        embed_list = discord.Embed(
            title="Nowe plany zajęć",
            colour=discord.Colour.red()
        )
        if len(new_plans) != 0:
            for plan in new_plans:
                embed_list.add_field(name=plan['semestr'], value=plan['link'], inline=False)
            await ctx.send(embed=embed_list)
        else:
            embed_list = discord.Embed(
                title="Nowe Plany zajęć",
                colour=discord.Colour.red()
            )
            embed_list.set_image(url='https://www.weeren.net/nothing.gif')
            await ctx.send(embed=embed_list)
    # Jeżeli wyświetlamy wszystkie plany
    else:
        embed_list = discord.Embed(
            title="Plany zajęć",
            colour=discord.Colour.blue()
        )
        if len(new_plans) != 0:
            for plan in new_plans:
                embed_list.add_field(name=plan['semestr'], value=plan['link'], inline=False)
            await ctx.send(embed=embed_list)
        else:
            embed_list = discord.Embed(
                title="Plany zajęć",
                colour=discord.Colour.blue()
            )
            embed_list.set_image(url='https://www.weeren.net/nothing.gif')
            await ctx.send(embed=embed_list)


bot.run(os.getenv('BOT_TOKEN'))


import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from scrape import PlanScraperForApocryph

load_dotenv()

bot = commands.Bot(command_prefix='^', description='First iteration of Apocryph')


@bot.event
async def on_ready():
    print("I'm ready!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="students suffer"))


@bot.command()
async def plan_zajec(ctx):
    plan = PlanScraperForApocryph()
    plan.get_plan()
    await ctx.send(file=discord.File(fp='Plans/PlanJPGS/plan.jpg'))



bot.run(os.getenv('BOT_TOKEN'))


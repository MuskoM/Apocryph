import discord
import dotenv
from discord.ext import commands
from scrape import PlanScraperForApocryph

bot = commands.Bot(command_prefix='^', description='First iteration of Apocryph')

@bot.event
async def on_ready():
    print("I'm ready!")
    print(bot.user.name)
    print(bot.user.id)


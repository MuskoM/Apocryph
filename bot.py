import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='=', description='Bot wspomagający studentów PB w zdobyciu inżyniera', owner_id=168274679457513473)

bot.load_extension('Plany')
bot.load_extension('ListaZadan')

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

bot.run(os.getenv('XENO_TOKEN'))


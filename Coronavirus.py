import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

class Coronavirus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="koronawirus")
    async def covid(self, ctx, *args):
        """
        Wyświetla aktualne zachorowania na koronawirusa
        """
        site = requests.get(url="https://www.worldometers.info/coronavirus/")
        soup = BeautifulSoup(site.content, 'html.parser')
        embedded = discord.Embed(
            title="Coronavirus cases",
            colour=discord.Colour.dark_red()
        )

        countries = soup.find('tbody').find_all('tr')
        for i in countries:
            if i.text.strip().startswith('Poland'):
                lista = i.text.strip().split()
                embedded.add_field(name='Kraj', value=lista[0])
                embedded.add_field(name='Przypadki', value=lista[1])
                if lista[2].startswith("+"):
                    embedded.add_field(name='Nowe przypadki', value=lista[2])

        updateTime = soup.find_all(class_='container')[1].find_all(class_='row')[1].find(style="font-size:13px; color:#999; text-align:center").text
        wynik = soup.find_all(class_='container')[1].find_all(class_='row')[1].find_all(id='maincounter-wrap')

        # embedded.add_field(name=updateTime)
        # for i in wynik:
        #     embedded.add_field(name=i.text)

        await ctx.send(embed=embedded)


def setup(bot):
    bot.add_cog(Coronavirus(bot))
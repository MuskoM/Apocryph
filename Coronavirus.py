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
        Wyświetla aktualne zachorowania na koronawirusa w Polsce
        """
        site = requests.get(url="https://epidemia-koronawirus.pl")
        soup = BeautifulSoup(site.content, 'html.parser')
        allCases = soup.find(id="panel-2-0-0-0").find(style="font-size: 48px;").text.strip().split()
        curedCases = soup.find(id="panel-2-0-1-0").find(style="font-size: 48px;").text.strip().split()
        deadCases = soup.find(id="panel-2-0-2-0").find(style="font-size: 48px;").text.strip().split()
        embedded = discord.Embed(
            title="Coronavirus cases in Poland",
            colour=discord.Colour.dark_red(),
        )
        embedded.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1024px-SARS-CoV-2_without_background.png")
        embedded.set_footer(text="Source: epidemia-koronawirus.pl")

        embedded.add_field(name="All cases", value=allCases[0])
        embedded.add_field(name="Cured cases", value=curedCases[0])
        embedded.add_field(name="Dead cases", value=deadCases[0])

        await ctx.send(embed=embedded)

    @commands.command(name="powiaty")
    async def covidPowiaty(self, ctx, *args):
        """
        Wyświetla link do mapy z przypadkami koronawirusa w poszczególnych powiatach.
        :param ctx:
        :param args:
        :return:
        """
        embedded = discord.Embed(
            title="Przypadki koronawirusa w powiatach",
            colour=discord.Colour.dark_red(),
        )
        embedded.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1024px-SARS-CoV-2_without_background.png")
        embedded.add_field(name="Link do strony", value="https://bit.ly/2zSjHp3")

        await ctx.send(embed=embedded)


def setup(bot):
    bot.add_cog(Coronavirus(bot))

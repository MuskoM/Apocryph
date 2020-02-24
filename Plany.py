import discord
from discord.ext import commands
from scrape import PlanScraperForApocryph


class Plany(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.plan_scraper = PlanScraperForApocryph()

    @commands.command(name="plan",
                      aliases=['plan_zajec'])
    async def plan(self, ctx):
        """
        Wyświetla plan zajęć dla naszego semestru
        """
        self.plan_scraper.get_plan()
        await ctx.send(file=discord.File(fp='Plans/PlanJPGS/plan.jpg'))

    @commands.command(name="planSemestrow",
                      aliases=['spisPlanow'])
    async def planySemestrow(self, ctx):
        """
        Wyświetla plany wszystkich semestrów I stopnia
        """
        plans = self.plan_scraper.fresh_plans(False)
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


def setup(bot):
    bot.add_cog(Plany(bot))

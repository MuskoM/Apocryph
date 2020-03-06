import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()


class Janitor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_owner(self):
        return self.bot.get_user(168274679457513473)

    def is_bot(self, m):
        m.author == self.bot

    @commands.command(name="wipe",
                      aliases=['prune', 'cls'],
                      usage="\nPierwszy parametr: liczba wiadomości do usunięcia\n"
                            "Drugi parametr: przy braku parametru usuwa wszystkie "
                            "albo wspomnianego użytkownika",)
    async def purge(self, ctx, num_of_msg, who='all'):
        """
        Usuwa wiadomości z kanału
        """
        await ctx.message.delete()
        counter = 0
        if who is 'all':
            deleted = await ctx.channel.purge(limit=int(num_of_msg))
            await ctx.channel.send(f"Deleted {len(deleted)} messages", delete_after=5)
        else:
            async for message in ctx.channel.history(limit=int(num_of_msg)):
                if who == message.author.mention:
                    await message.delete()
                    counter += 1
            await ctx.channel.send(f"Deleted {counter} messages from user: {who}", delete_after=5)


def setup(bot):
    bot.add_cog(Janitor(bot))

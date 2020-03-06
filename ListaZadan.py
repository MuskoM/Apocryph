import discord
from discord.ext import commands
import os


class ListaZadan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dodajZadanie",
                      aliases=['dz'],
                      usage="\nPierwszy parametr: nagłówek zadania\n"
                            "Drugi parametr(W \"\"): Cel zadania "
                      )
    async def dodajZadanie(self, ctx, *args):
        """
        Dodaje zadanie do listy
        """
        await ctx.send(f'**Dodano zadanie** {args[0]}\n'
                       f'**Cel:** {args[1]}')
        try:
            quests = open('etc/quests.txt', 'a')
        except FileNotFoundError:
            quests = open('etc/quests.txt', 'w')
        for item in args:
            quests.write(f'{item} ')
        quests.write('\n')

    @commands.command(name="wyświetlZadania",
                      aliases=['wz'],
                      usage="Funkcja bez parametrów\n"
                      )
    async def wyswietlZadania(self, ctx):
        """
        Wyświetla listę zadań
        """
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

    @commands.command(name="usunZadanie",
                      aliases=['uz'],
                      usage="Pierwszy parametr: numer zadania do usunięcia, \n"
                            "[all] usuwa wszystkie zadania z listy\n"
                      )
    async def usunZadanie(self, ctx, indx):
        """
        Usuwa zadanie/a z listy
        """
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


def setup(bot):
    bot.add_cog(ListaZadan(bot))
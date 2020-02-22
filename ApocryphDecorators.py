from discord.ext import commands


def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 576064030666653710
    return commands.check(predicate)
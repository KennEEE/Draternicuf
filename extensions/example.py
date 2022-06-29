import hikari
import lightbulb
import json

class Music():
    def __init__(self):
        pass


plugin = lightbulb.Plugin('Example')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)

@plugin.command
@lightbulb.command('pee', 'says poop')
@lightbulb.implements(lightbulb.SlashCommand)
async def pee(ctx):
    await ctx.respond('Poop!')


def load(bot):
    bot.add_plugin(plugin)

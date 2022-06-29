import lightbulb
import hikari



bot = lightbulb.BotApp(token='OTkxNDA5MDQ0MDc2MTIyMTEy.G-Yui4.uuaQSTexefJdJezXA8RTc_pxs7XFuKEzb61Xik', 
default_enabled_guilds=(438828400422027264))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Draternicuf has Started!')

@bot.command
@lightbulb.command('ping', 'Says Pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx): #all commands take in context ctx = context
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')

@bot.command
@lightbulb.option('num1', 'The First Number', type = int)
@lightbulb.option('num2', 'The Second Number', type = int)
@lightbulb.command('add', 'Add two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.load_extensions_from('./extensions')

bot.run()
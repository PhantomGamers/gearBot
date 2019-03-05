import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys,keys
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound

#Makes the traceback 1 line.
sys.tracebacklimit = 0

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.gear','cogs.gearhelp']

bot = commands.Bot(command_prefix='!', description='gearBot')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


#Displays the bots tags and ID in terminal
async def on_ready():
    print("\n".join(
        ["#" * 25, "Name:{0.name}#{0.discriminator}".format(bot.user), "Id : {}".format(bot.user.id), "#" * 25]))


#The main function of bot, any new features will clearget made with cogs, which has already been implemented.


#Silences the error commands if someone using a command this bot doesn't support with it's prefex.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
    
#Pass your bots api key here
bot.run(keys.gearBot)
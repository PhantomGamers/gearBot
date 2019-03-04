
import discord
from discord.ext import commands
import sys, traceback



# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.gearhelp',]

bot = commands.Bot(command_prefix='.', description='A Rewrite Cog Example')

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


#Example of the structure of a command
@bot.command()
async def example(ctx):
    """ This is how you set a comment in !help for the command"""
    await ctx.send('Hey there!')



#Pass your bots api key here
bot.run('MzMyNzE2ODgwNTM4MTA3OTA1.DzfmAw.1ycYIdRu0MutuabfixikelR-NrU')
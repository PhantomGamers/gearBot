import discord
from discord.ext import commands
from fractions import gcd

#Put standard operations here, such a gcd etc...

class gearhelp_Cog(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='gcd')
    async def gcd(self):
        """ Produle help docs for the bot. """
        await ctx.send('Help me!')


#Adding this as a cog
def setup(bot):
    bot.add_cog(gearhelp_Cog(bot))
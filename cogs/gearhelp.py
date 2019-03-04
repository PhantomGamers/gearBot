import discord
from discord.ext import commands
from fractions import gcd

#Put standard operations here, such a gcd etc...

class gearhelp_Cog(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='gcd')
    async def gcd(self, ctx, xx, yy):
        """ Produces the GCD of the first number passed. """
        x = int(xx)
        y = int(yy)
        while y != 0:
            (x, y) = (y, x % y)
        await ctx.send('GCD of first number: {}'.format(x,y))




#Adding this as a cog
def setup(bot):
    bot.add_cog(gearhelp_Cog(bot))
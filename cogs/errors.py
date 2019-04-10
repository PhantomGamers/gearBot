import traceback
import sys
from discord.ext import commands
import discord
import asyncio


class errors_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Join the gearbot support channel", colour=discord.Colour(0xa9219b), url="https://discord.gg/jZAJ7Yy")

            #embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")
            embed.set_author(name="n0tj#6859", url="https://n0tj.com", icon_url="https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")
            embed.set_footer(text="Message n0tj#6859 with any bugs or concerns.", icon_url="https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")

            embed.add_field(name="Updating your gear screenshot, direct link only", value="**!gear <link>**")
            embed.add_field(name="Looking up someone or your own gear", value="**!gear <@user>**")


            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(errors_Cog(bot))

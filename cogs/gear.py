import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys
from cogs.modules import db_sessions, urlChecker, logger
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class gear_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='gear')
    async def gear(self, ctx, args):
        """First update your gear with !gear <link> then query your gear and other players with !gear <@user>"""
        user = ctx.author
        str_user = str(user)
        test = await db_sessions.sql_id(args)


        if args.startswith("<"):
            getTag = discord.utils.get(
                        ctx.message.guild.members, id=ctx.message.raw_mentions[0])
            w = await db_sessions.sql_name(str(getTag))
            if str(getTag) == w:
                #Check to see weather they can have a direct link or not and then chooses the format based on that.
                some_list = [await db_sessions.sql_link(str(getTag))]
                extensions = ['.jpg', '.png', '.PNG', '.JPG']
                flag = 0
                for s in some_list:
                    for item in extensions:
                        if item in s:
                            flag = 1
                if flag == 0:
                        #Legacy layout
                        print(("User mention: {}").format(str(ctx.author.mention)))
                        await ctx.send("{} 's gear: {}".format(args, await db_sessions.sql_link(str(getTag))))
                        #Logging
                        await logger.bigLog.log_5(ctx,str_user,str(getTag))
                else:
                    #Fancy frame for displaying user gear, ap and dp.
                    embed = discord.Embed(colour=discord.Colour(0xa9219b))
                    embed.set_image(url=await db_sessions.sql_link(str(getTag)))
                    embed.set_thumbnail(url="https://pbs.twimg.com/media/DIF3WFMVwAA1qAN.png")
                    embed.set_author(name="get gearBot",  url="https://discordbots.org/bot/344643767313235968", icon_url="https://pbs.twimg.com/media/DIF3WFMVwAA1qAN.png")
                    embed.set_footer(text=test, icon_url= "https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")
                    await ctx.send( embed=embed)
                    #Logging
                    await logger.bigLog.log_6(ctx,str_user,str(getTag))       
            else:
                await ctx.send("{} isn't in the database. Type !gearhelp for more information.".format(args))
                print("{} isn't in the database.".format(args))


        #This is some santization of input, when the user passes a link it verifies it is a link by checking to see if its starts with 'http'
        #Try to cover more edge cases here for example if the user passes an invalid link or if they pass garbage instead of a link or a users @.
        if await urlChecker.urlCheck(urlChecker.session, args) is False:
            await ctx.send("Hey, your link is invalid.")
        else:
            if args.startswith("http") and await urlChecker.urlCheck(urlChecker.session, args) is True:

                r = await db_sessions.sql_check_name_v2(str(user))
                if str_user == r:
                    await db_sessions.sql_update_link(str_user, args)
                    await ctx.send("{} gear has been updated.".format("<@" + str(ctx.author.id) + ">"))
                    #Logging
                    await logger.bigLog.log_1(ctx,str_user)
                else:
                    await db_sessions.sql_new_user(str(user), args, "<@" + str(ctx.author.id) + ">")
                    await ctx.send("You have been added to the database.")
                    #Logging
                    await logger.bigLog.log_2(ctx,str_user)
            
            if args.startswith("http") or args.startswith("<"):
                print("User invoked command.")
            else:
                embed = discord.Embed(colour=discord.Colour(0xa9219b))
                embed.set_thumbnail(url="https://pbs.twimg.com/media/DIF3WFMVwAA1qAN.png")
                embed.set_author(name="Join the gearBot discord", url="https://discord.gg/jZAJ7Yy", icon_url="https://pbs.twimg.com/media/DIF3WFMVwAA1qAN.png")
                embed.set_footer(text="Message n0tj#6859 with any bugs or concerns.", icon_url="https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")
                embed.add_field(name="**Updating your gear screenshot, direct link only**", value="**!gear <link>**")
                embed.add_field(name="**Looking up someone or your own gear**", value="**!gear <@user>**")
                await ctx.send(embed=embed)
                            


#Adding this as a cog
def setup(bot):
    bot.add_cog(gear_Cog(bot))
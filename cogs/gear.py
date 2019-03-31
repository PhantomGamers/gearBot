import discord,aiomysql,aiohttp,async_timeout,asyncio,traceback,sys
from cogs.modules import db_sessions, urlChecker, logger
import datetime
from datetime import date
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class gear_Cog(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='gear')
    async def gear(self, ctx, args):
        user = ctx.author
        str_user = str(user)
  
        if args.startswith("<"):
            getTag = discord.utils.get(
                        ctx.message.guild.members, id=ctx.message.raw_mentions[0])
            w = await db_sessions.sql_name(str(getTag))
            if str(getTag) == w:
                #Check to see weather they can have a direct link or not and then chooses the format based on that.
                some_list = [await db_sessions.sql_link(str(getTag))]
                bad = ['.jpg', '.png']
                flag = 0
                for s in some_list:
                    for item in bad:
                        if item in s:
                            flag = 1
                if flag == 0:
                        #Legacy layout
                        print(("User mention: {}").format(str(ctx.author.mention)))
                        await ctx.send("{} 's gear: {}".format("@" + str(getTag), await db_sessions.sql_link(str(getTag))))
                        #Logging
                        await logger.bigLog.log_5(ctx,str_user,str(getTag))
                else:
                    #Fancy frame for displaying user gear, ap and dp.
                    embed = discord.Embed()
                    embed.set_image(url=await db_sessions.sql_link(str(getTag)))
                    embed.set_thumbnail(url=getTag.avatar_url)
                    embed.set_author(name=str(getTag), icon_url=getTag.avatar_url)
                    embed.set_footer(text="n0tj#6859 with bugs", icon_url= "https://pbs.twimg.com/profile_images/1111417292955381761/z18vzMwY_400x400.png")
                    await ctx.send( embed=embed)
                #Logging
                    await logger.bigLog.log_6(ctx,str_user,str(getTag))
                    #print(user.mentioned_in(message))
                    #print(ctx.message.raw_mentions) #this returns the mentions ID.
                    #print(ctx.message.guild.name) # Returns the guild that user used the command in. Should also add a timestamp when this is put in a database. So they can only change guild every 48hrs
                    #print("\n".join([x.name for x in role.members])) #LIST OF ALL THE USERS IN A ROLE          
            else:
                await ctx.send("User {} isn't in the database.".format(str(getTag)))
                print("User {} isn't in the database.".format(str(getTag)))



        #This is some santization of input, when the user passes a link it verifies it is a link by checking to see if its starts with 'http'
        if args.startswith("http") and await urlChecker.urlCheck(urlChecker.session, args) is True:
            r = await db_sessions.sql_check_name_v2(str(user))
            if str_user == r:
                await db_sessions.sql_update_link(str_user, args)
                await ctx.send("Your gear has been updated.")
                #Logging
                await logger.bigLog.log_1(ctx,str_user)
            else:
                await db_sessions.sql_new_user(str(user), args, "<@" + str(ctx.author.id) + ">")
                await ctx.send("You have been added to the database.")
                #Logging
                await logger.bigLog.log_2(ctx,str_user)
        else:
            await ctx.send("Invalid URL, please try a different one.")
                   



#Adding this as a cog
def setup(bot):
    bot.add_cog(gear_Cog(bot))
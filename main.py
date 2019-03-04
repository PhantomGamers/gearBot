import discord
import aiomysql
import db_sessions
import aiohttp
import async_timeout
import datetime
from datetime import date
import asyncio
import keys
import sys
from discord.ext import commands
import logging
import logger
import urlChecker
import traceback
from discord.ext.commands import CommandNotFound

#Makes the traceback 1 line.
sys.tracebacklimit = 0

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.gearhelp',]

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



#The main function of bot, any new features will get made with cogs, which has already been implemented.
@bot.command()
async def gear(ctx, args, ap=None, dp=None):
    user = ctx.author
    str_user = str(user)

    #This is some santization of input, when the user passes a link it verifies it is a link by checking to see if its starts with 'http'
    if args.startswith("http") and await urlChecker.urlCheck(urlChecker.session, args) is True:
        if ap == None or dp == None:
            r = await db_sessions.sql_check_name_v2(str(user))
            if str_user == r:
                await db_sessions.sql_update_link(str_user, args)
                await ctx.send("You gear has been updated.")
                #Logging
                await logger.bigLog.log_1(ctx,str_user)
            else:
                await db_sessions.sql_new_user(str(user), args, "<@" + str(ctx.author.id) + ">")
                await ctx.send("You have been added to the database.")
                #Logging
                await logger.bigLog.log_2(ctx,str_user)
        else:
            # Currently you must pass both AP and DP for it to update the DB, if you just do one it wont do anything.
            # Not currently implemented.
            if int(ap) > 290 or int(dp) > 420:
                await ctx.send("Please enter correct data. You cheeky cunt.")
                #Logging
                await logger.bigLog.log_3(ctx,str_user)
            else:
                await ctx.send("You have updated your ap & dp.")
                await logger.bigLog.log_4(ctx,str_user)
    else:
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
                        #await ctx.send("Note: {}".format(await db_sessions.sql_get_note(str(getTag))))
                        #Logging
                        await logger.bigLog.log_5(ctx,str_user,str(getTag))
                else:
                    #Fancy frame for displaying user gear, ap and dp.
                    embed = discord.Embed()
                    embed.set_image(url=await db_sessions.sql_link(str(getTag)))
                    embed.set_thumbnail(url=getTag.avatar_url)
                    embed.set_author(name=str(getTag), icon_url=getTag.avatar_url)
                    embed.set_footer(text="n0tj#6859 with bugs", icon_url= "https://n0tj.com/files/z.jpg")
                    #embed.add_field(name="Note", value= await db_sessions.sql_get_note(str(getTag)))
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
        else:
            await ctx.send("Bad URL, please try a different one.")

#Silences the error commands if someone using a command this bot doesn't support with it's prefex.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
    


#Pass your bots api key here
bot.run(keys.gearBot)
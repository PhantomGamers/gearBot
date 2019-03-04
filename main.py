import discord
import settings
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

# TODO: Under !gear @, I figured out the logic on how to do the !mainServer command.
# TODO: Also under !gear @, I figured out how to get the ID from the mention'd.

bot = commands.Bot(command_prefix=settings.command_prefix)



@bot.event
async def on_ready():
    print("\n".join(
        ["#" * 25, "Name:{0.name}#{0.discriminator}".format(bot.user), "Id : {}".format(bot.user.id), "#" * 25]))


@bot.event
async def on_guild_join(guild):
    await guild.create_role(name="gearBot Mod")
    print("done")

@bot.event
async def on_guild_join(guild):
    await guild.create_role(name="gearBot User")
    print("done")


#Main convert break up into cogs later.
@bot.command()
async def gear(ctx, args, ap=None, dp=None):
    user = ctx.author
    str_user = str(user)

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




def checkMe(ctx):
    return ctx.message.author.id == 105714191653949440


@bot.command()
@commands.check(checkMe)
async def exit(ctx):
    """Closes the bot."""
    await ctx.send("Logging out!")
    await bot.logout()


@bot.command()
async def version(ctx):
    await ctx.send(str(discord.__version__))

# Left off with building the add new note insert in db_sessions
@bot.command()
async def gearnote(ctx, args):
    user = ctx.author
    str_user = str(user)
    r = await db_sessions.sql_check_name_v2(str(user))
    note = await db_sessions.sql_check_note(str(user))
    if note == 'None':

        await db_sessions.sql_new_user_note(str(user), "<@" + str(ctx.author.id) + ">", str(args))
        await ctx.send("You have been added to the database.")
                #Make an update note in db_sessions

    else:
        await db_sessions.sql_update_note(str_user, args)
        await ctx.send("Your note has been updated.")
        print(await db_sessions.sql_check_note(str_user))
                    #Logging
                    #await logger.bigLog.log_1(ctx,str_user)




@bot.command()
async def gearhelp(ctx):
    """ Explains how to use this bot."""
    user = ctx.author
    str_user = str(user)
    #Fancy frame for displdaying
    embed = discord.Embed(title="", colour=discord.Colour(0x36990), url="https://discordapp.com/oauth2/authorize?client_id=344643767313235968&scope=bot&permissions=0x10008000)", description="`> ` [Patch Notes.](https://www.n0tj.com/gearbot.html) \n > [Get gearBot.](https://discordapp.com/oauth2/authorize?client_id=344643767313235968&scope=bot&permissions=0x10008000) \n > [Github.](https://github.com/n0tj/gearBot) ")
    embed.set_thumbnail(url="https://n0tj.com/files/z.jpg")
    #embed.set_author(name="gearbot help", url="", icon_url="")
    embed.set_footer(text="n0tj#6859 with bugs")
    await ctx.send(embed=embed)
    #Logging
    await logger.bigLog.log_7(ctx,str_user)


bot.run(keys.gearBot)

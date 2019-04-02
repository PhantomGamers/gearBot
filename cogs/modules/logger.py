import discord
from discord.ext import commands
import aiomysql
import db_sessions
import datetime
import logging

#Rewrote the logging writing to a file, but the issue is that it will only write to the file after,
#  the bot restarts which is bad and dumb.
time = datetime.datetime.now() #This change fixes the time issue where it was displaying the wrong time
f = open("log.txt", "a")

class bigLog:
    async def log_1(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print("Valid Link.")
        print("{} is in the database.".format(str_user))
        print ("{} updated their gear link.".format(str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        f.write("{}: Updated {} link! \n".format(time,str_user))
      
    async def log_2(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} has been added to the database.".format(str_user))
        print("{}: Queries:{} {}".format(time,await db_sessions.sql_get_counter(), await db_sessions.sql_counter()))
        f.write("{}: {} has been added to the database! \n".format(time,str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        
    async def log_3(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} tried to update their ap or dp with invalid data".format(str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        f.write("{}: {} tried to update with invalid AP and or DP. \n".format(time,str_user))
      
    async def log_4(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} updated their gear, ap and dp.".format(str_user))
        f.write("{}: {} updated their ap and dp! \n".format(time,str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
    
    async def log_5(ctx,str_user,getTag):
        print("##########################")
        print("Legacy Layout")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user, getTag))
        f.write("{}: {} looked up {} with the legacy layout. \n".format(time,str_user,getTag))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
   
    async def log_6(ctx,str_user,getTag):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user,getTag))
        f.write("{}: {} looked up {} with the improved layout. \n".format(time,str_user,getTag))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
   
    async def log_7(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} toggled gearhelp!".format(str_user))

    async def log_8(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} toggled link help!".format(str_user))

import discord
from discord.ext import commands
import aiomysql
import db_sessions
import datetime
import logging


time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
logging.basicConfig(filename='bigLog.log',level=logging.INFO)


class bigLog:
    async def log_1(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print("Good Link.")
        print("User did not update AP & DP.")
        print("{} is in the database.".format(str_user))
        print ("{} updated their gear link.".format(str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("{}: Updated {} link!".format(time,str_user))
        logging.info("##########################")

    async def log_2(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} has been added to the database.".format(str_user))
        print("{}: Queries:{} {}".format(time,await db_sessions.sql_get_counter(), await db_sessions.sql_counter()))
        logging.info("{}: {} has been added to the database!".format(time,str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("##########################")

    async def log_3(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} tried to update their ap or dp with invalid data".format(str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("{}: {} tried to update with invalid AP and or DP.".format(time,str_user))
        logging.info("##########################")

    async def log_4(ctx,str_user):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} updated their gear, ap and dp.".format(str_user))
        logging.info("{}: {} updated their ap and dp!".format(time,str_user))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("##########################")

    async def log_5(ctx,str_user,getTag):
        print("##########################")
        print("Legacy Layout")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user, getTag))
        logging.info("{}: {} looked up {} with the legacy layout.".format(time,str_user,getTag))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("##########################")

    async def log_6(ctx,str_user,getTag):
        print("##########################")
        print(time)
        print("Server: {}".format(ctx.guild))
        print ("{} looked up {}'s gear".format(str_user,getTag))
        logging.info("{}: {} looked up {} with the improved layout.".format(time,str_user,getTag))
        await db_sessions.sql_counter()
        print("{}: Queries: {}".format(time,await db_sessions.sql_get_counter()))
        logging.info("##########################")

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

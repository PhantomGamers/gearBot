import dbl
import discord
from discord.ext import commands
import aiohttp
import asyncio
import logging

class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = 'dbl_token'  #  set this to your DBL token, update this if bot gets verified.
        self.dblpy = dbl.Client(self.bot, self.token, loop=bot.loop)
        self.updating = bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        await self.bot.is_ready()
        while not bot.is_closed():
            logger.info('Attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('Posted server count ({})'.format(self.dblpy.guild_count())
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
                await asyncio.sleep(1800)

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
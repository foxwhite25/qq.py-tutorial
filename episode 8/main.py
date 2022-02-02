import logging
import os
import random
from typing import Optional, Dict

import colorlog
from qq.ext import commands
import qq
from config import appid, token

intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix='/', intents=intent, owner_id=2229785998145077655)

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(name)-15s] [%(levelname)-7s]: %(message)s (%(filename)s:%(lineno)d)",
        "%Y-%m-%d %H:%M:%S")
)

logger = logging.getLogger('qq')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

for each in os.listdir('./cogs'):
    if each.endswith('.py'):
        bot.load_extension(f'cogs.{each[:-3]}')


@bot.command(hidden=True)
async def reload(self, ctx: commands.Context, ext: str):
    self.bot.reload_extension(ext)
    logger.info(f"Ext {ext} loaded")


@bot.command(hidden=True)
async def unload(self, ctx: commands.Context, ext: str):
    self.bot.unload_extension(ext)
    logger.info(f"Ext {ext} unloaded")


@bot.command(hidden=True)
async def load(self, ctx: commands.Context, ext: str):
    self.bot.load_extension(ext)
    logger.info(f"Ext {ext} loaded")


if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")

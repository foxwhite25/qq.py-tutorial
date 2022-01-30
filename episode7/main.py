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
bot = commands.Bot(command_prefix='/', intents=intent, owner_id=114514)

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


@bot.command()
async def reload(ctx: commands.Context, ext: str):
    bot.reload_extension(ext)
    await ctx.reply(f"Ext {ext} loaded")


@bot.command()
async def unload(ctx: commands.Context, ext: str):
    bot.unload_extension(ext)
    await ctx.reply(f"Ext {ext} unloaded")


@bot.command()
async def load(ctx: commands.Context, ext: str):
    bot.load_extension(ext)
    await ctx.reply(f"Ext {ext} loaded")


if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")

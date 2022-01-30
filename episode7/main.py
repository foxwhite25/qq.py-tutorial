import logging
import os

import colorlog
from qq.ext import commands
import qq

intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix='/', intents=intent)

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(name)-15s] [%(levelname)-7s]: %(message)s (%(filename)s:%(lineno)d)",
        "%Y-%m-%d %H:%M:%S")
)

logger = logging.getLogger('qq')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# for each in os.listdir('./cogs'):
#     if each.endswith('.py'):
#         bot.load_extension(f'cogs.{each[:-3]}')

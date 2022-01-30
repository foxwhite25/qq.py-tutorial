import re
from typing import Optional

import qq
from qq.ext import commands
from qq.ext.commands import Greedy

from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)
client = qq.Client()
intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix="/", owner_id=114514, intents=intent)


@bot.command(name="test2")
async def test(ctx: commands.Context, string: str):
    await ctx.reply(string)

if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")

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


@bot.group()
async def git(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.reply(f'缺失参数')


@git.command()
async def pull(ctx, url: str):
    await ctx.reply(f"成功从{url}抓取")


@git.command()
async def clone(ctx, url: str):
    await ctx.reply(f"成功从{url}复制")


@git.command()
async def push(ctx, url: str):
    await ctx.reply(f"成功推送至{url}")


if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")

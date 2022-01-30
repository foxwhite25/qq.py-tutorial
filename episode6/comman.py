import qq
from qq.ext import commands
from qq.ext.commands import CommandOnCooldown, CheckFailure

from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)
client = qq.Client()
intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix="/", owner_id=114514, intents=intent)


@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.reply(str(error))
    if isinstance(error, CheckFailure):
        await ctx.reply(str(error))


@bot.check
async def is_a_in_message(ctx: commands.Context):
    return "a" in ctx.message.content


@commands.cooldown(rate=1, per=10, type=commands.BucketType.member)
@bot.command(name="foo")
async def test2(ctx: commands.Context, string: str):
    raise AttributeError
    await ctx.reply(string)


@test2.error
async def test2_error(ctx: commands.Context, error):
    await ctx.reply(f"test2 errored {error}")


@commands.cooldown(rate=1, per=10, type=commands.BucketType.member)
@bot.command(name="bar")
async def test(ctx: commands.Context, string: str):
    raise AttributeError
    await ctx.reply(string)


@test.error
async def test_error(ctx: commands.Context, error):
    await ctx.reply(f"test errored {error}")


@bot.group()
async def git(ctx: commands.Context):
    if not ctx.subcommand_passed:
        await ctx.reply("无效参数")


@git.command()
async def pull(ctx: commands.Context, url: str):
    await ctx.reply(f"pull {url}")


@git.command()
async def clone(ctx: commands.Context, url: str):
    await ctx.reply(f"clone {url}")


if __name__ == '__main__':
    bot.run(token=f"{appid}.{token}")

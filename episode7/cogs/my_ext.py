import logging
import random
from typing import Optional, Dict

from qq.ext import commands

logger = logging.getLogger('qq.my_ext')


class Eco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.money: Dict[int, int] = {}

    def add_money(self, member_id, count):
        if member_id not in self.money:
            self.money[member_id] = 0
        self.money[member_id] += count

    def remove_money(self, member_id, count):
        if member_id not in self.money:
            self.money[member_id] = 0
        self.money[member_id] -= count

    def is_enough_money(self, member_id, count):
        if member_id not in self.money:
            self.money[member_id] = 0
        return self.money[member_id] >= count


class MyCogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("my_ext loaded")

    async def cog_command_error(self, ctx: commands.Context, error: Exception) -> None:
        print(error)

    @commands.command()
    async def foo(self, ctx: commands.Context, string: Optional[str]):
        if string:
            await ctx.reply(string)
        else:
            await ctx.reply('bar')

    @commands.command()
    async def add_money(self, ctx: commands.Context, count: int):
        eco: Eco = self.bot.get_cog("Eco")
        eco.add_money(ctx.author.id, count)
        await ctx.reply(f"成功添加{count}金钱")

    @commands.command()
    async def gamble(self, ctx: commands.Context, count: int):
        eco: Eco = self.bot.get_cog("Eco")
        if eco.is_enough_money(ctx.author.id, count):
            eco.remove_money(ctx.author.id, count)
            if random.randint(0, 1):
                eco.add_money(ctx.author.id, int(count * 1.5))
                await ctx.reply(f"赢了{count * 1.5}")
            else:
                await ctx.reply(f"你输了 {count}")
        else:
            await ctx.reply("你没有足够金钱")

    @commands.command()
    async def check(self, ctx: commands.Context):
        eco: Eco = self.bot.get_cog("Eco")
        if ctx.author.id in eco.money:
            await ctx.reply(f"{eco.money[ctx.author.id]}")


def setup(bot: commands.Bot):
    bot.add_cog(MyCogs(bot))
    bot.add_cog(Eco(bot))


def teardown(bot: commands.Bot):
    print("Teardown")

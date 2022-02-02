from typing import Optional

from qq.ext import commands


class StringOp(commands.Cog):
    """字符串相关处理"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(help='把两个字符串组合在一起')
    async def combine(self, ctx: commands.Context, a: str, b: Optional[str]):
        await ctx.reply(a + b)

    @commands.command(name='split', aliases=['separate'], help='把两个字符串按照后面的参数分开')
    async def _split(self, ctx: commands.Context, a: str, b: str):
        await ctx.reply(str(a.split(b)))


def setup(bot):
    bot.add_cog(StringOp(bot))

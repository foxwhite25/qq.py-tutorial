from qq.ext import commands


class MathOp(commands.Cog):
    """数学相关处理"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['plus'], help='加两个数')
    async def add(self, ctx: commands.Context, a: int, b: int):
        await ctx.reply(str(a + b))

    @commands.command(aliases=['subtract'], help='减两个数')
    async def minus(self, ctx: commands.Context, a: int, b: int):
        await ctx.reply(str(a - b))

    @commands.command(aliases=['multiply'])
    async def times(self, ctx: commands.Context, a: int, b: int):
        """乘两个数
        第二行只是为了好看
        """
        await ctx.reply(str(a * b))

    @commands.command()
    async def divide(self, ctx: commands.Context, a: int, b: int):
        """除两个数"""
        await ctx.reply(str(a / b))


def setup(bot):
    bot.add_cog(MathOp(bot))

from typing import Optional

from qq.ext import commands


class Help(commands.Cog):
    """显示帮助信息"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.command()
    async def help(self, ctx:commands.Context, input: Optional[str], extra: Optional[str]):
        """参数: <拓展名>
        显示所有的模块以及指令"""
        prefix = self.bot.command_prefix

        owner = 2229785998145077655
        version = "v1.0.0"

        if not input:

            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            result = f"指令与模块:\n使用 `{prefix}help <模块>` 来获取关于该模块的更多资讯 😀\n\n "

            cogs_doc = ""
            for cogs_name, cogs in self.bot.cogs.items():
                cogs_doc += f"`{cogs_name}` {cogs.description}\n"

            result += f"模块:\n{cogs_doc}\n\n"

            commands_desc = ""
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f"{command.name} - {command.help}\n"

            if commands_desc:
                result += f"不属于模块的指令\n {commands_desc} \n\n"

            result += "关于:\n这个机器人由 foxwhite25 基于 qq\ufeff.py 开发。\n" \
                      f"目前这个版本由 {owner} 维护\n" \
                      f"如果要提交错误报告或建议请前往 github /foxwhite25/qq\ufeff.py-tutorial\n" \
                      f"机器人运行于版本 {version}。"

        elif not extra:

            for cog_name, cogs in self.bot.cogs.items():

                if cog_name.lower() == input.lower():

                    result = f"{cog_name} - 指令\n{cogs.description}\n\n"

                    for command in cogs.get_commands():
                        if not command.hidden:
                            result += f"{prefix}{command.name}\n{command.help}\n"
                    break

                else:
                    result = f"这是什么？！\n我从来没有见过一个叫 {input} 的模块 😱。"

        else:
            result = "这太多了！\n一次请只请求一个模块😀。"

        await ctx.reply(result)


def setup(bot):
    bot.add_cog(Help(bot))
import qq
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)
client = qq.Client()


@client.event
async def on_message(message: qq.Message):
    print(message.content)
    if "!i" in message.content:
        await message.reply("1234")
    if "!b" in message.content:
        await message.reply("4567")


@client.event
async def on_ready():
    print("使用机器人登陆成功。")


if __name__ == '__main__':
    client.run(token=f"{appid}.{token}")

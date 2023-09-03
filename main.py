import discord
import asyncio
import logging

from config import prefix, TOKEN, owner_id, colors
from utils.classes import ZhongWenBot


logging.basicConfig(level=logging.ERROR)


async def main():
    extensions = ("cogs." + ext for ext in ("util_commands", "zhong_commands"))
    bot_kwargs = {
        "owner_id": owner_id,
        "colors": colors,
    }
    intents = discord.Intents.default()
    bot = ZhongWenBot(prefix, intents=intents, **bot_kwargs)

    for ext in extensions:
        await bot.load_extension(ext)

    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())

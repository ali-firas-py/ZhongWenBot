from discord.ext import commands
import discord
import asyncio
import logging

from config import prefix, TOKEN, owner_id


logging.basicConfig(level=logging.ERROR)


class ZhongWenBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        print(f"Syncing app commands...")
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} commands.")

    async def on_ready(self):
        print(f"{self.user.name} is ready.\n")


async def main():
    extensions = ("cogs." + ext for ext in ("util_commands", "zhong_commands"))
    bot_kwargs = {
        "owner_id": owner_id,
    }
    intents = discord.Intents.default()
    bot = ZhongWenBot(prefix, intents=intents, **bot_kwargs)

    for ext in extensions:
        await bot.load_extension(ext)

    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())

from discord.ext import commands
from discord import app_commands, Interaction, Embed


class UtilCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="...")
    async def learn(self, interaction: Interaction):
        ...


async def setup(bot: commands.Bot):
    await bot.add_cog(UtilCommands(bot))

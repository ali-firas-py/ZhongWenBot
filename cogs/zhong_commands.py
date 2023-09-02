from discord.ext import commands
from discord import app_commands, Interaction, Embed

from utils.views import WikiView


class ZhongCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Lists characters and common phrases")
    async def wiki(self, interaction: Interaction, index: int=1):
        embed = Embed(title="Learning...", color=self.bot.green)
        await interaction.response.send_message(embed=embed, view=WikiView())


async def setup(bot: commands.Bot):
    await bot.add_cog(ZhongCommands(bot))

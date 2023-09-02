from discord.ext import commands
from discord import app_commands, Interaction, Embed


class ZhongCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="...")
    async def learn(self, interaction: Interaction):
        await interaction.response.send_message(embed=Embed(title="Learning...", color=self.bot.green))


async def setup(bot: commands.Bot):
    await bot.add_cog(ZhongCommands(bot))

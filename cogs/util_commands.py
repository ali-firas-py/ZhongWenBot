from discord.ext import commands
from discord import app_commands, Interaction, Embed

from utils.classes import ZhongWenBot


class UtilCommands(commands.Cog):
    def __init__(self, bot: ZhongWenBot):
        self.bot = bot

    @app_commands.command(description="Shows a list of commands.")
    async def help(self, interaction: Interaction):
        embed = Embed(title="ZhongWenBot Commands")

        for cog_name, cog in self.bot.cogs.items():
            app_cmds = [f"`/{cmd.name} {' '.join([param.name for param in cmd.parameters])}`: {cmd.description}" 
                        for cmd in cog.get_app_commands()]  # remember to handle hidden cmds
            embed.add_field(name=cog_name, value="\n".join(app_cmds))

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(UtilCommands(bot))

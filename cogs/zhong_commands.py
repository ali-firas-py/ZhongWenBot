from discord.ext import commands
from discord import app_commands, Interaction, Embed

from utils.views import WikiView
from utils.classes import ZhongWenBot


class ZhongCommands(commands.Cog):
    def __init__(self, bot: ZhongWenBot):
        self.bot = bot

    @app_commands.command(description="Lists characters and some common phrases.")
    async def wiki(self, interaction: Interaction, hide_info: bool = False, page: int=1):
        char = self.bot.Zi.hsk1.get(page)
        
        if char is None:
            return await interaction.response.send_message("Character not found.", ephemeral=True)

        if hide_info:
            description = f"Pinyin: ||{char.pinyin}||\nMeaning: ||{char.english}||"
            value = f"Pinyin: ||{char.sentence_pinyin}||\nMeaning: ||{char.sentence_english}||"
            embed = Embed(title=f"{char}", description=description, color=self.bot.green)
            embed.add_field(name=f"{char.sentence}", value=value)
        
        else:
            description = f"# {char} ({char.pinyin})\n{char.english}"
            embed = Embed(description, color=self.bot.green)
            embed.add_field(name=f"# {char.sentence} ({char.sentence_pinyin})", value=char.sentence_english)
            embed.set_footer(text=f"id: {char.id}")
            
        await interaction.response.send_message(embed=embed, view=WikiView(self.bot, page, hide_info))


async def setup(bot):
    await bot.add_cog(ZhongCommands(bot))

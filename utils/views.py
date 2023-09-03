from discord.ui import View, Button, button
from discord import ButtonStyle, Interaction, Embed

from utils.classes import ZhongWenBot


class WikiView(View):
    def __init__(self, bot: ZhongWenBot, page: int, hide_info: bool, timeout=120.0):
        self.bot = bot
        self.page = page
        self.pages = len(bot.Zi.hsk1)
        self.hide_info = hide_info

        super().__init__(timeout=timeout)

    async def update(self, interaction: Interaction):
        char = self.bot.Zi.hsk1.get(self.page)

        if self.hide_info:
            description = f"Pinyin: ||{char.pinyin}||\nMeaning: ||{char.english}||"
            value = f"Pinyin: ||{char.sentence_pinyin}||\nMeaning: ||{char.sentence_english}||"
            embed = Embed(title=f"{char}", description=description, color=self.bot.green)
            embed.add_field(name=f"{char.sentence}", value=value)
        
        else:
            description = f"# {char} ({char.pinyin})\n{char.english}"
            embed = Embed(description, color=self.bot.green)
            embed.add_field(name=f"# {char.sentence} ({char.sentence_pinyin})", value=char.sentence_english)
            embed.set_footer(text=f"id: {char.id}")
    
        await interaction.response.edit_message(embed=embed)

    @button(style=ButtonStyle.blurple, custom_id="previous", emoji="⬅️")
    async def previous(self, interaction: Interaction, button: Button):
        self.page = (self.pages + self.page - 1) % self.pages
        await self.update(interaction)

    @button(style=ButtonStyle.blurple, custom_id="next", emoji="➡️")
    async def next(self, interaction: Interaction, button: Button):
        self.page = (self.pages + self.page + 1) % self.pages
        await self.update(interaction)

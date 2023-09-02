from discord.ui import View, Button, button
from discord import ButtonStyle, Interaction, Embed
from discord.ext.commands import Bot


class WikiView(View):
    def __init__(self, *, page: int, timeout=120.0):
        self.page = page
        self.chars = ['a', 'b', 'c', 'd']
        super().__init__(timeout=timeout)

    async def update(self, interaction: Interaction):
        embed = Embed(title=self.chars[self.page - 1])
        
        if self.page == 1:
            embed.set_footer(text="Hint: you can jump to any page by choosing an index (ex: /wiki 42)")

        await interaction.response.edit_message(embed=embed)

    @button(style=ButtonStyle.blurple, custom_id="previous", emoji="⬅️")
    async def previous(self, interaction: Interaction, button: Button):
        self.page = (self.page - 1) % len(self.chars)
        await self.update(interaction)

    @button(style=ButtonStyle.blurple, custom_id="next", emoji="➡️")
    async def next(self, interaction: Interaction, button: Button):
        self.page = (self.page + 1) % len(self.chars)
        await self.update(interaction)

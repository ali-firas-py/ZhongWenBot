from discord.ui import View, Button, button
from discord import ButtonStyle, Interaction
from discord.ext.commands import Bot


class WikiView(View):
    def __init__(self, *, timeout=120.0):
        super().__init__(timeout=timeout)

    @button(style=ButtonStyle.blurple, custom_id="previous", emoji="⬅️")
    async def previous(self, interaction: Interaction, button: Button):
        await interaction.response.send_message("goin left")

    @button(style=ButtonStyle.blurple, custom_id="next", emoji="➡️")
    async def next(self, interaction: Interaction, button: Button):
        await interaction.response.send_message("goin right")

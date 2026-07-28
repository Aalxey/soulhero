import discord

from bot.story.prologue import get_prologue_page
from bot.views.prologue_view import PrologueView


class ArrivalView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

        button = discord.ui.Button(
            label="📖 Read the Chronicle",
            style=discord.ButtonStyle.primary
        )

        button.callback = self.read_chronicle

        self.add_item(button)

    async def read_chronicle(
        self,
        interaction: discord.Interaction
    ):
        embed = get_prologue_page(1)

        await interaction.response.edit_message(
            embed=embed,
            view=PrologueView()
        )
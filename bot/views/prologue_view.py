import discord
from bot.story.prologue import get_prologue_page


class PrologueView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.current_page = 1

    @discord.ui.button(
    label="Next ▶",
    style=discord.ButtonStyle.primary
    )
    async def next_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if self.current_page < 4:
            self.current_page += 1

        embed = get_prologue_page(self.current_page)

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )
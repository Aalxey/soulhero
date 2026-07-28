import discord

from bot.story.prologue import get_prologue_page
from bot.story.soul_core import get_soul_core_embed
from bot.views.soul_core_view import SoulCoreView



class PrologueView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.current_page = 1

        # Previous Button
        self.previous_button = discord.ui.Button(
            label="◀ Previous",
            style=discord.ButtonStyle.primary
        )
        self.previous_button.callback = self.previous_callback

        # Next Button
        self.next_button = discord.ui.Button(
            label="Next ▶",
            style=discord.ButtonStyle.primary
        )
        self.next_button.callback = self.next_callback

        # Add buttons to the view
        self.add_item(self.previous_button)
        self.add_item(self.next_button)

        # Set the initial button state
        self.update_buttons()

    def update_buttons(self):
        """Update button states based on the current page."""

        # Previous Button
        self.previous_button.disabled = self.current_page == 1

        # Last Page
        if self.current_page == 4:
            self.next_button.label = "Step Forward"
            self.next_button.style = discord.ButtonStyle.success
        else:
            self.next_button.label = "Next ▶"
            self.next_button.style = discord.ButtonStyle.primary

    async def previous_callback(self, interaction: discord.Interaction):
        if self.current_page > 1:
            self.current_page -= 1

        self.update_buttons()

        embed = get_prologue_page(self.current_page)

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    async def next_callback(self, interaction: discord.Interaction):
        if self.current_page < 4:
            self.current_page += 1

            self.update_buttons()

            embed = get_prologue_page(self.current_page)

            await interaction.response.edit_message(
                embed=embed,
                view=self
            )
        else:
            embed = get_soul_core_embed()

            await interaction.response.edit_message(
                embed=embed,
                view=SoulCoreView()
            )
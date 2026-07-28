import discord

from bot.story.prologue import get_prologue_page
from bot.story.soul_core import get_soul_core_embed
from bot.views.soul_core_view import SoulCoreView


class PrologueView(discord.ui.View):

    def __init__(self, player_id: int):

        super().__init__(timeout=None)

        self.player_id = player_id
        self.current_page = 1


        self.previous_button = discord.ui.Button(
            label="◀ Previous",
            style=discord.ButtonStyle.primary
        )

        self.previous_button.callback = (
            self.previous_callback
        )


        self.next_button = discord.ui.Button(
            label="Next ▶",
            style=discord.ButtonStyle.primary
        )

        self.next_button.callback = (
            self.next_callback
        )


        self.add_item(
            self.previous_button
        )

        self.add_item(
            self.next_button
        )


        self.update_buttons()



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        """
        Only the owner of this Forgotten Ruins
        memory can interact with it.
        """

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 This memory does not belong to your soul.",
                ephemeral=True
            )

            return False


        return True



    def update_buttons(self):

        self.previous_button.disabled = (
            self.current_page == 1
        )


        if self.current_page == 4:

            self.next_button.label = (
                "Step Forward"
            )

            self.next_button.style = (
                discord.ButtonStyle.success
            )

        else:

            self.next_button.label = (
                "Next ▶"
            )

            self.next_button.style = (
                discord.ButtonStyle.primary
            )



    async def previous_callback(
        self,
        interaction: discord.Interaction
    ):

        if self.current_page > 1:

            self.current_page -= 1


        self.update_buttons()


        embed = get_prologue_page(
            self.current_page
        )


        await interaction.response.edit_message(
            embed=embed,
            view=self
        )



    async def next_callback(
        self,
        interaction: discord.Interaction
    ):

        if self.current_page < 4:

            self.current_page += 1


            self.update_buttons()


            embed = get_prologue_page(
                self.current_page
            )


            await interaction.response.edit_message(
                embed=embed,
                view=self
            )

            return



        # Last page reached
        # Player enters Soul Core

        embed = get_soul_core_embed()


        await interaction.response.edit_message(
            embed=embed,
            view=SoulCoreView(
                player_id=self.player_id
            )
        )
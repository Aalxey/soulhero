import discord

from bot.story.prologue import get_prologue_page
from bot.views.prologue_view import PrologueView


class ArrivalView(discord.ui.View):

    def __init__(
        self,
        player_id: int
    ):

        super().__init__(
            timeout=None
        )

        self.player_id = player_id


        button = discord.ui.Button(
            label="📖 Read the Chronicle",
            style=discord.ButtonStyle.primary
        )


        button.callback = (
            self.read_chronicle
        )


        self.add_item(button)



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 This chronicle does not belong to your soul.",
                ephemeral=True
            )

            return False


        return True



    async def read_chronicle(
        self,
        interaction: discord.Interaction
    ):

        embed = get_prologue_page(1)


        await interaction.response.edit_message(

            embed=embed,

            view=PrologueView(
                player_id=self.player_id
            )

        )
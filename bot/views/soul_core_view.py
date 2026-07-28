import discord

from bot.views.sleeping_hall_view import SleepingHallView
from bot.story.sleeping_hall import get_sleeping_hall_embed


class SoulCoreView(discord.ui.View):

    def __init__(self, player_id: int):

        super().__init__(timeout=None)

        self.player_id = player_id


        self.answer_button = discord.ui.Button(
            label="🜂 Answer the Call",
            style=discord.ButtonStyle.success
        )


        self.answer_button.callback = (
            self.answer_callback
        )


        self.add_item(
            self.answer_button
        )



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        """
        Only the owner of this Soul Core
        can awaken their Hero.
        """

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 The Soul Core rejects your presence.",
                ephemeral=True
            )

            return False


        return True



    async def answer_callback(
        self,
        interaction: discord.Interaction
    ):

        view = SleepingHallView(
            player_id=self.player_id
        )


        hero = view.get_current_hero()


        embed = get_sleeping_hall_embed(
            hero
        )


        await interaction.response.edit_message(
            embed=embed,
            view=view
        )
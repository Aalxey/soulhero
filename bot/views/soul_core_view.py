import discord
from bot.views.sleeping_hall_view import SleepingHallView
from bot.story.sleeping_hall import get_sleeping_hall_embed
from bot.story.soul_core import get_soul_core_embed


class SoulCoreView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

        self.answer_button = discord.ui.Button(
            label="🜂 Answer the Call",
            style=discord.ButtonStyle.success
        )

        self.answer_button.callback = self.answer_callback

        self.add_item(self.answer_button)

    async def answer_callback(
        self,
        interaction: discord.Interaction
    ):
        view = SleepingHallView()
        hero = view.get_current_hero()

        embed = get_sleeping_hall_embed(hero)

        await interaction.response.edit_message(
            embed=embed,
            view=view
        )
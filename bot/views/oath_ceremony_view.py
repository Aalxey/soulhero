import discord

from bot.views.welcome_view import WelcomeView
from bot.services.player_service import PlayerService
from bot.utils.constants import JourneyState
from bot.story.oath_dialogue import get_oath_dialogue


class OathCeremonyView(discord.ui.View):

    def __init__(self, hero):

        super().__init__(
            timeout=None
        )

        self.hero = hero



    @discord.ui.button(
        label="⚔ Accept the Oath",
        style=discord.ButtonStyle.success
    )
    async def accept_oath(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        player = PlayerService.get_player(
            interaction.user.id
        )


        if player is None:

            await interaction.response.send_message(

                "The Soul Core cannot find your existence.",

                ephemeral=True

            )

            return



        if player.hero_id is None:

            await interaction.response.send_message(

                "No sleeping soul has answered your call yet.",

                ephemeral=True

            )

            return



        if player.journey_state == JourneyState.OATH_COMPLETE:

            await interaction.response.send_message(

                "Your oath has already been formed.",

                ephemeral=True

            )

            return



        PlayerService.complete_oath(
            interaction.user.id
        )


        dialogue = get_oath_dialogue(
            self.hero
        )


        embed = discord.Embed(

            title=f"⚔ Oath Formed — {self.hero['name']}",

            description=dialogue["complete"],

            color=discord.Color.gold()

        )


        embed.set_footer(

            text="The ruins still await your final trial."

        )


        await interaction.response.edit_message(

            embed=embed,

            view=WelcomeView(self.hero)

        )
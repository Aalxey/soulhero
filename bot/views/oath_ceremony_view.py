import discord

from bot.views.welcome_view import WelcomeView
from bot.services.player_service import PlayerService
from bot.utils.constants import JourneyState
from bot.story.oath_dialogue import get_oath_dialogue


class OathCeremonyView(discord.ui.View):

    def __init__(
        self,
        hero,
        player_id: int
    ):

        super().__init__(
            timeout=None
        )

        self.hero = hero
        self.player_id = player_id



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        # Only the owner of this oath can continue

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 This oath does not belong to your soul.",
                ephemeral=True
            )

            return False


        return True



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
            self.player_id
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



        if (
            player.journey_state
            == JourneyState.OATH_COMPLETE
        ):

            await interaction.response.send_message(
                "Your oath has already been formed.",
                ephemeral=True
            )

            return



        PlayerService.complete_oath(
            self.player_id
        )


        dialogue = get_oath_dialogue(
            self.hero
        )


        embed = discord.Embed(

            title=(
                f"⚔ Oath Formed — "
                f"{self.hero['name']}"
            ),

            description=dialogue["complete"],

            color=discord.Color.gold()

        )


        embed.set_footer(
            text="The ruins still await your final trial."
        )


        await interaction.response.edit_message(

            embed=embed,

            view=WelcomeView(
                self.hero,
                self.player_id
            )

        )
import discord

from bot.services.player_service import PlayerService
from bot.utils.constants import JourneyState


class RuinsCollapseView(discord.ui.View):

    def __init__(
        self,
        hero,
        player_id: int,
        channel
    ):

        super().__init__(
            timeout=None
        )

        self.hero = hero
        self.player_id = player_id
        self.channel = channel



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 This trial does not belong to your soul.",
                ephemeral=True
            )

            return False


        return True



    @discord.ui.button(
        label="🔱 Break the Ancient Seal",
        style=discord.ButtonStyle.danger
    )
    async def collapse_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        player = PlayerService.get_player(
            self.player_id
        )


        if player is None:

            await interaction.response.send_message(
                "The ruins cannot find your existence.",
                ephemeral=True
            )

            return



        if (
            player.journey_state
            != JourneyState.WELCOME
        ):

            await interaction.response.send_message(
                "The seal refuses to answer.",
                ephemeral=True
            )

            return



        PlayerService.collapse_ruins(
            self.player_id
        )


        embed = discord.Embed(

            title="🌑 The Ancient Seal Breaks",

            description=(

                "The Forgotten Ruins tremble...\n\n"

                "The ancient chains binding this place "
                "begin to shatter.\n\n"

                "The oath you carried is no longer "
                "a promise.\n\n"

                "It is a bond.\n\n"

                "**You are now OATHBOUND.**"

            ),

            color=discord.Color.dark_purple()

        )


        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


        # Remove the Forgotten Ruins after collapse

        try:

            await self.channel.delete(
                reason="Forgotten Ruins collapsed after Oathbound awakening."
            )

        except discord.Forbidden:
            pass

        except discord.NotFound:
            pass
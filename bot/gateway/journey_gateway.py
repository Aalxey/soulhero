import discord

from bot.services.channel_service import ChannelService
from bot.services.journey_service import JourneyService
from bot.services.player_service import PlayerService

from bot.story.arrival import get_arrival_embed
from bot.story.welcome_story import get_welcome_story

from bot.utils.constants import JourneyState

from bot.views.arrival_view import ArrivalView
from bot.views.welcome_view import WelcomeView


class JourneyGateway:

    @staticmethod
    async def resume(
        interaction: discord.Interaction,
        player,
        bot
    ):

        scene = JourneyService.get_scene(
            player
        )

        # ---------------------------------
        # First Arrival
        # ---------------------------------

        if scene == "ARRIVAL":

            await JourneyGateway._arrival(

                interaction,

                bot

            )

            return

        # ---------------------------------
        # Sleeping Hall
        # ---------------------------------

        if scene == "SLEEPING_HALL":

            channel = await JourneyGateway._get_channel(

                interaction,

                bot

            )

            await interaction.response.send_message(

                (
                    "🌑 Your awakening remains unfinished.\n\n"
                    f"Continue your journey in {channel.mention}."
                ),

                ephemeral=True

            )

            return

        # ---------------------------------
        # Oath Ceremony
        # ---------------------------------

        if scene == "OATH":

            channel = await JourneyGateway._get_channel(

                interaction,

                bot

            )

            await interaction.response.send_message(

                (
                    "⚔ Your oath has not yet been completed.\n\n"
                    f"Return to {channel.mention}."
                ),

                ephemeral=True

            )

            return

        # ---------------------------------
        # Welcome
        # ---------------------------------

        if scene == "WELCOME":

            hero = JourneyService.get_player_hero(
                player
            )

            if hero is None:

                await interaction.response.send_message(

                    "Your Hero could not be found.",

                    ephemeral=True

                )

                return

            channel = await JourneyGateway._get_channel(

                interaction,

                bot

            )

            # Prevent duplicate Welcome messages

            await interaction.response.send_message(

                (
                    "🌒 Your oath has been acknowledged.\n\n"
                    f"Continue your journey in {channel.mention}."
                ),

                ephemeral=True

            )

            return

        # ---------------------------------
        # Ruins Collapse
        # ---------------------------------

        if scene == "COLLAPSE":

            channel = await JourneyGateway._get_channel(

                interaction,

                bot

            )

            await interaction.response.send_message(

                (
                    "🌋 The Ancient Seal still awaits.\n\n"
                    f"Return to {channel.mention}."
                ),

                ephemeral=True

            )

            return

        # ---------------------------------
        # Soul World
        # ---------------------------------

        if scene == "SOUL_WORLD":

            await interaction.response.send_message(

                (
                    "⚔ You are already Oathbound.\n\n"
                    "The Forgotten Ruins have fallen behind you.\n\n"
                    "Your story now continues in Soul World."
                ),

                ephemeral=True

            )

            return

    @staticmethod
    async def _arrival(

        interaction,

        bot

    ):

        channel = await JourneyGateway._get_channel(

            interaction,

            bot

        )

        await channel.send(

            embed=get_arrival_embed(),

            view=ArrivalView(

                player_id=interaction.user.id

            )

        )

        # -------------------------------
        # Checkpoint
        # -------------------------------

        PlayerService.update_journey_state(

            str(interaction.user.id),

            JourneyState.AWAKENING

        )

        await interaction.response.send_message(

            (
                "🜂 The Forgotten Ruins have opened before you.\n\n"
                f"Your path awaits in {channel.mention}."
            ),

            ephemeral=True

        )

    @staticmethod
    async def _get_channel(

        interaction,

        bot

    ):

        bot_member = interaction.guild.get_member(

            bot.user.id

        )

        return await ChannelService.get_or_create_awakening_chamber(

            guild=interaction.guild,

            member=interaction.user,

            bot_member=bot_member

        )
import discord

from bot.utils.constants import JourneyState

from bot.services.player_service import PlayerService
from bot.services.channel_service import ChannelService
from bot.services.soul_chamber_service import SoulChamberService

from bot.engine.scene_manager import SceneManager

from bot.scenes.arrival_scene import ArrivalScene
from bot.scenes.welcome_scene import WelcomeScene
from bot.scenes.collapse_scene import CollapseScene

from bot.views.arrival_view import ArrivalView
from bot.story.arrival import get_arrival_embed


class JourneyGateway:
    """
    Responsible only for deciding where a player's journey continues.

    It does NOT:
        - build embeds
        - build views
        - handle buttons
        - write SQL

    It only routes the player to the correct Scene and the correct World.
    """



    @staticmethod
    async def resume(
        interaction: discord.Interaction,
        player,
        bot
    ):

        state = player.journey_state



        # ---------------------------------
        # FIRST ARRIVAL
        # ---------------------------------

        if state == JourneyState.WANDERER:


            await JourneyGateway._arrival(

                interaction,

                bot,

                player

            )


            return



        # ---------------------------------
        # AWAKENING
        # ---------------------------------

        if state == JourneyState.AWAKENING:


            channel = await JourneyGateway._get_ruins_channel(

                interaction,

                bot

            )


            await interaction.response.send_message(

                (
                    "🌑 Your awakening remains unfinished.\n\n"
                    f"Your forgotten path awaits in {channel.mention}."
                ),

                ephemeral=True

            )


            return



        # ---------------------------------
        # HERO CHOSEN
        # ---------------------------------

        if state == JourneyState.HERO_CHOSEN:


            channel = await JourneyGateway._get_ruins_channel(

                interaction,

                bot

            )


            await interaction.response.send_message(

                (
                    "⚔ Your oath ceremony remains incomplete.\n\n"
                    f"Your Hero awaits you in {channel.mention}."
                ),

                ephemeral=True

            )


            return



        # ---------------------------------
        # OATH COMPLETE
        # SHOW WELCOME SCENE
        # ---------------------------------

        if state == JourneyState.OATH_COMPLETE:


            hero = PlayerService.get_player_hero(

                interaction.user.id

            )


            if hero is None:


                await interaction.response.send_message(

                    "The bond between soul and hero cannot be found.",

                    ephemeral=True

                )


                return



            channel = await JourneyGateway._get_ruins_channel(

                interaction,

                bot

            )


            scene = WelcomeScene(

                player,

                hero

            )


            await SceneManager.send(

                channel,

                scene

            )


            await interaction.response.send_message(

                f"🌒 Your oath has been acknowledged. Continue your journey in {channel.mention}.",

                ephemeral=True

            )


            return




        # ---------------------------------
        # WELCOME COMPLETE
        # SHOW COLLAPSE SCENE
        # ---------------------------------

        if state == JourneyState.WELCOME:


            hero = PlayerService.get_player_hero(

                interaction.user.id

            )


            if hero is None:


                await interaction.response.send_message(

                    "Your hero bond cannot be found.",

                    ephemeral=True

                )


                return



            channel = await JourneyGateway._get_ruins_channel(

                interaction,

                bot

            )


            scene = CollapseScene(

                player,

                hero

            )


            await SceneManager.send(

                channel,

                scene

            )


            await interaction.response.send_message(

                f"🌋 The final trial awaits in {channel.mention}.",

                ephemeral=True

            )


            return




        # ---------------------------------
        # OATHBOUND
        # ---------------------------------

        if state == JourneyState.OATHBOUND:

            chamber = await JourneyGateway._get_soul_chamber(

                interaction,

                bot

            )

            await interaction.response.send_message(

                (

                    "🌑 Welcome back, Oathbearer.\n\n"

                    f"Your Soul Chamber awaits in {chamber.mention}."

                ),

                ephemeral=True

            )

            return




    @staticmethod
    async def _arrival(

        interaction,

        bot,

        player

    ):


        channel = await JourneyGateway._get_ruins_channel(

            interaction,

            bot

        )


        scene = ArrivalScene(

            player

        )


        await SceneManager.send(

            channel,

            scene

        )


        PlayerService.update_state(

            str(interaction.user.id),

            JourneyState.AWAKENING

        )


        await interaction.response.send_message(

            f"🜂 Your path awaits in {channel.mention}.",

            ephemeral=True

        )




    @staticmethod
    async def _get_ruins_channel(

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


    @staticmethod
    async def _get_soul_chamber(

        interaction,

        bot

    ):

        bot_member = interaction.guild.get_member(

            bot.user.id

        )

        return await SoulChamberService.get_or_create(

            guild=interaction.guild,

            member=interaction.user,

            bot_member=bot_member

        )
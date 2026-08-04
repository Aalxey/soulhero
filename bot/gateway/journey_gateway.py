import discord

from bot.utils.constants import JourneyState

from bot.services.player_service import PlayerService
from bot.services.channel_service import ChannelService
from bot.services.soul_chamber_service import SoulChamberService
from bot.services.scene_recovery_service import SceneRecoveryService

from bot.scenes.arrival_scene import ArrivalScene
from bot.scenes.welcome_scene import WelcomeScene
from bot.scenes.collapse_scene import CollapseScene
from bot.scenes.oath_scene import OathScene


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

        try:

            state = player.journey_state

            print(
                "CURRENT JOURNEY STATE:",
                player.journey_state,
                type(player.journey_state)
            )



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

                await SceneRecoveryService.restore(

                    player,

                    channel,

                    ArrivalScene

                )

                await interaction.followup.send(

                    (
                        "🌑 Your awakening continues...\n\n"
                        f"Your path awaits in {channel.mention}."
                    ),

                    ephemeral=True

                )

                return



            # ---------------------------------
            # HERO CHOSEN
            # ---------------------------------

            if state == JourneyState.HERO_CHOSEN:

                print("➡ HERO CHOSEN: Restoring Oath Scene")


                hero = PlayerService.get_player_hero(
                    interaction.user.id
                )


                if hero is None:

                    await interaction.followup.send(

                        "⚠ Your Hero bond cannot be found.",

                        ephemeral=True

                    )

                    return



                channel = await JourneyGateway._get_ruins_channel(

                    interaction,

                    bot

                )


                await SceneRecoveryService.restore(

                    player,

                    channel,

                    OathScene,

                    hero

                )


                await interaction.followup.send(

                    (
                        "⚔ Your oath ceremony has been restored.\n\n"
                        f"Continue your destiny in {channel.mention}."
                    ),

                    ephemeral=True

                )


                return



            # ---------------------------------
            # OATH COMPLETE
            # SHOW COLLAPSE SCENE
            # ---------------------------------

            if state == JourneyState.OATH_COMPLETE:

                hero = PlayerService.get_player_hero(

                    interaction.user.id

                )

                if hero is None:

                    await interaction.followup.send(

                        "The bond between soul and hero cannot be found.",

                        ephemeral=True

                    )

                    return

                channel = await JourneyGateway._get_ruins_channel(

                    interaction,

                    bot

                )

                await SceneRecoveryService.restore(

                    player,

                    channel,

                    CollapseScene,

                    hero

                )

                await interaction.followup.send(

                    f"⚔ The ancient seal fractures. Continue in {channel.mention}.",

                    ephemeral=True

                )

                return




            if state == JourneyState.COLLAPSE:

                hero = PlayerService.get_player_hero(

                    interaction.user.id

                )

                if hero is None:

                    await interaction.followup.send(

                        "Your hero bond cannot be found.",

                        ephemeral=True

                    )

                    return

                channel = await JourneyGateway._get_ruins_channel(

                    interaction,

                    bot

                )

                await SceneRecoveryService.restore(

                    player,

                    channel,

                    WelcomeScene,

                    hero

                )

                await interaction.followup.send(

                    f"🌒 Welcome to the Soul Chamber in {channel.mention}.",

                    ephemeral=True

                )

                return




            # ---------------------------------
            # WELCOME
            # ---------------------------------

            if state == JourneyState.WELCOME:

                chamber = await JourneyGateway._get_soul_chamber(

                    interaction,

                    bot

                )

                await interaction.followup.send(

                    (
                        "🌒 You have entered a new realm.\n\n"
                        f"Your Soul Chamber awaits in {chamber.mention}."
                    ),

                    ephemeral=True

                )

                return




            # ---------------------------------
            # OATHBOUND
            # ---------------------------------

            if state == JourneyState.OATHBOUND:

                print("2. Getting hero")

                hero = PlayerService.get_player_hero(interaction.user.id)

                print("3. Getting chamber")

                chamber = await JourneyGateway._get_soul_chamber(
                    interaction,
                    bot
                )

                print("4. Ready for Soul World")

                # TODO: Create SoulWorldScene for OATHBOUND players
                # For now, just acknowledge they are in the chamber
                # await SceneRecoveryService.restore(
                #     player,
                #     chamber,
                #     SoulWorldScene,
                #     hero
                # )

                print("5. Chamber ready")

                await interaction.followup.send(
                    f"🌑 Welcome back to your Soul Chamber in {chamber.mention}.",
                    ephemeral=True
                )

                print("6. Followup sent")

                return


            print(
                "⚠ UNKNOWN JOURNEY STATE:",
                state
            )

        except Exception:
            import traceback
            print("\n" + "="*60)
            print("❌ ERROR IN JOURNEY GATEWAY")
            print("="*60)
            traceback.print_exc()
            print("="*60 + "\n")




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

        await SceneRecoveryService.restore(

            player,

            channel,

            ArrivalScene

        )

        PlayerService.update_state(

            str(interaction.user.id),

            JourneyState.AWAKENING

        )

        player.journey_state = JourneyState.AWAKENING

        await interaction.followup.send(

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
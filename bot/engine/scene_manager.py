import discord

from bot.engine.message_manager import MessageManager


class SceneManager:
    """
    Responsible for displaying scenes.

    SceneManager never knows:

    - Story
    - Hero
    - SQL
    - JourneyState
    - Battle Logic

    It only renders Scene objects.
    """

    @staticmethod
    async def send(
        channel: discord.TextChannel,
        scene
    ):

        print(
            "SCENE SEND START:",
            scene.scene_name,
            "CHANNEL:",
            channel.name
        )

        embed = scene.build_embed()
        view = scene.build_view()

        print(
            "EMBED CREATED:",
            embed.title
        )

        print(
            "VIEW CREATED:",
            type(view).__name__
            if view
            else "None"
        )

        message = await channel.send(

            embed=embed,

            view=view

        )

        print(
            "SCENE MESSAGE SENT:",
            message.id
        )

        # -----------------------------------
        # Allow views to know their message
        # (used by timeout handlers)
        # -----------------------------------

        if view is not None:
            view.message = message

        # -----------------------------------
        # Save Journey Scenes
        # -----------------------------------

        if hasattr(scene, "player"):

            MessageManager.save(

                discord_id=scene.player.discord_id,

                channel_id=channel.id,

                message_id=message.id,

                scene_name=scene.scene_name

            )

        # -----------------------------------
        # Save Battle Scene
        # -----------------------------------

        elif hasattr(scene, "battle"):

            MessageManager.save(

                discord_id=scene.battle.player_one.discord_id,

                channel_id=channel.id,

                message_id=message.id,

                scene_name=scene.scene_name

            )

            MessageManager.save(

                discord_id=scene.battle.player_two.discord_id,

                channel_id=channel.id,

                message_id=message.id,

                scene_name=scene.scene_name

            )

        print(
            "MESSAGE SAVED"
        )

        return message

    @staticmethod
    async def edit(
        interaction: discord.Interaction,
        scene
    ):

        print(
            "SCENE EDIT:",
            scene.scene_name
        )

        await interaction.response.edit_message(

            embed=scene.build_embed(),

            view=scene.build_view()

        )

        # -----------------------------------
        # Journey Scene
        # -----------------------------------

        if hasattr(scene, "player"):

            MessageManager.save(

                discord_id=scene.player.discord_id,

                channel_id=interaction.channel.id,

                message_id=interaction.message.id,

                scene_name=scene.scene_name

            )

        # -----------------------------------
        # Battle Scene
        # -----------------------------------

        elif hasattr(scene, "battle"):

            MessageManager.save(

                discord_id=scene.battle.player_one.discord_id,

                channel_id=interaction.channel.id,

                message_id=interaction.message.id,

                scene_name=scene.scene_name

            )

            MessageManager.save(

                discord_id=scene.battle.player_two.discord_id,

                channel_id=interaction.channel.id,

                message_id=interaction.message.id,

                scene_name=scene.scene_name

            )

    @staticmethod
    async def resend(
        channel: discord.TextChannel,
        scene
    ):

        return await SceneManager.send(

            channel,

            scene

        )
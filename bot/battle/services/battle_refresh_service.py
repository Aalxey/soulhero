import discord

from bot.scenes.battle_scene import BattleScene


class BattleRefreshService:
    """
    Responsible ONLY for refreshing
    the battle message.

    Responsibilities:
        - Fetch battle message
        - Rebuild BattleScene
        - Edit Discord message

    Never:
        - Calculate damage
        - Decide turns
        - Record wins
        - Give Resonance
    """

    @staticmethod
    async def refresh(
        interaction: discord.Interaction,
        battle,
        result=None
    ):

        guild = interaction.guild

        if guild is None:
            return

        channel = guild.get_channel(
            battle.channel_id
        )

        if channel is None:
            return

        try:

            message = await channel.fetch_message(
                battle.message_id
            )

        except discord.NotFound:
            return

        scene = BattleScene(

            battle=battle,

            result=result

        )

        await message.edit(

            embed=scene.build_embed(),

            view=scene.build_view()

        )
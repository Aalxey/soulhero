import discord

from discord.ext import commands
from discord import app_commands

from bot.services.player_service import PlayerService
from bot.services.battle_channel_service import BattleChannelService

from bot.battle.battle_manager import BattleManager


class Battle(commands.Cog):

    def __init__(
        self,
        bot
    ):

        self.bot = bot


    @app_commands.command(
        name="battle",
        description="Challenge another Oathbearer."
    )
    async def battle(

        self,

        interaction: discord.Interaction,

        member: discord.Member

    ):

        # -------------------------
        # Cannot battle yourself
        # -------------------------

        if member.id == interaction.user.id:

            await interaction.response.send_message(

                "⚔ You cannot challenge yourself.",

                ephemeral=True

            )

            return


        # -------------------------
        # Cannot battle bots
        # -------------------------

        if member.bot:

            await interaction.response.send_message(

                "⚔ You cannot challenge a bot.",

                ephemeral=True

            )

            return


        player_one = PlayerService.get_player(

            str(interaction.user.id)

        )

        player_two = PlayerService.get_player(

            str(member.id)

        )


        # -------------------------
        # Both players must exist
        # -------------------------

        if player_one is None:

            await interaction.response.send_message(

                "Begin your journey first with **/start**.",

                ephemeral=True

            )

            return


        if player_two is None:

            await interaction.response.send_message(

                f"{member.display_name} has not yet awakened.",

                ephemeral=True

            )

            return


        # -------------------------
        # Both players must be
        # Oathbound
        # -------------------------

        if not PlayerService.is_oathbound(

            str(interaction.user.id)

        ):

            await interaction.response.send_message(

                "Only Oathbearers may battle.",

                ephemeral=True

            )

            return


        if not PlayerService.is_oathbound(

            str(member.id)

        ):

            await interaction.response.send_message(

                f"{member.display_name} is not yet an Oathbearer.",

                ephemeral=True

            )

            return


        # -------------------------
        # Already battling?
        # -------------------------

        if BattleManager.is_in_battle(

            str(interaction.user.id)

        ):

            await interaction.response.send_message(

                "You are already in a battle.",

                ephemeral=True

            )

            return


        if BattleManager.is_in_battle(

            str(member.id)

        ):

            await interaction.response.send_message(

                f"{member.display_name} is already battling.",

                ephemeral=True

            )

            return


        # -------------------------
        # Create Battle
        # -------------------------

        battle = BattleManager.create(

            player_one,

            player_two

        )


        bot_member = interaction.guild.get_member(

            self.bot.user.id

        )


        channel = await BattleChannelService.create(

            guild=interaction.guild,

            battle=battle,

            player_one=interaction.user,

            player_two=member,

            bot_member=bot_member

        )


        battle.channel_id = channel.id


        await interaction.response.send_message(

            f"⚔ Battle created in {channel.mention}.",

            ephemeral=True

        )


async def setup(bot):

    await bot.add_cog(

        Battle(bot)

    )
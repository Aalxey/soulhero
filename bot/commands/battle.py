import traceback

import discord

from discord.ext import commands
from discord import app_commands

from bot.services.player_service import PlayerService
from bot.services.challenge_channel_service import ChallengeChannelService

from bot.battle.battle_manager import BattleManager

from bot.scenes.challenge_scene import ChallengeScene
from bot.engine.scene_manager import SceneManager


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

        try:

            print("=" * 60)
            print("⚔ /battle command started")
            print("=" * 60)

            await interaction.response.defer(
                ephemeral=True
            )

            print("1. Interaction deferred")

            # -------------------------
            # Cannot battle yourself
            # -------------------------

            if member.id == interaction.user.id:

                await interaction.followup.send(

                    "⚔ You cannot challenge yourself.",

                    ephemeral=True

                )

                return

            # -------------------------
            # Cannot battle bots
            # -------------------------

            if member.bot:

                await interaction.followup.send(

                    "⚔ You cannot challenge a bot.",

                    ephemeral=True

                )

                return

            print("2. Checking players")

            player_one = PlayerService.get_player(

                str(interaction.user.id)

            )

            player_two = PlayerService.get_player(

                str(member.id)

            )

            print("3. Players loaded")

            # -------------------------
            # Both players must exist
            # -------------------------

            if player_one is None:

                await interaction.followup.send(

                    "Begin your journey first with **/start**.",

                    ephemeral=True

                )

                return

            if player_two is None:

                await interaction.followup.send(

                    f"{member.display_name} has not yet awakened.",

                    ephemeral=True

                )

                return

            # -------------------------
            # Both players must be Oathbound
            # -------------------------

            if not PlayerService.is_oathbound(

                str(interaction.user.id)

            ):

                await interaction.followup.send(

                    "Only Oathbearers may battle.",

                    ephemeral=True

                )

                return

            if not PlayerService.is_oathbound(

                str(member.id)

            ):

                await interaction.followup.send(

                    f"{member.display_name} is not yet an Oathbearer.",

                    ephemeral=True

                )

                return

            print("4. Both players are Oathbound")

            # -------------------------
            # Already battling?
            # -------------------------

            if BattleManager.is_in_battle(

                str(interaction.user.id)

            ):

                await interaction.followup.send(

                    "You are already in a battle.",

                    ephemeral=True

                )

                return

            if BattleManager.is_in_battle(

                str(member.id)

            ):

                await interaction.followup.send(

                    f"{member.display_name} is already battling.",

                    ephemeral=True

                )

                return

            print("5. Creating challenge room")

            bot_member = interaction.guild.get_member(

                self.bot.user.id

            )

            channel = await ChallengeChannelService.create(

                guild=interaction.guild,

                challenger=interaction.user,

                challenged=member,

                bot_member=bot_member

            )

            print("6. Challenge room:", channel.name)

            hero = PlayerService.get_player_hero(

                str(interaction.user.id)

            )

            print("7. Hero:", hero["name"])

            scene = ChallengeScene(

                player_one,

                player_two,

                hero

            )

            print("8. Scene created")

            await SceneManager.send(

                channel,

                scene

            )

            print("9. Scene sent")

            await interaction.followup.send(

                f"📜 Challenge delivered in {channel.mention}.",

                ephemeral=True

            )

            print("10. Finished successfully")

        except Exception:

            print("\n" + "=" * 60)
            print("❌ BATTLE COMMAND ERROR")
            print("=" * 60)
            traceback.print_exc()
            print("=" * 60 + "\n")

            try:

                await interaction.followup.send(

                    "Something went wrong while creating the duel.",

                    ephemeral=True

                )

            except Exception:

                pass


async def setup(bot):

    await bot.add_cog(

        Battle(bot)

    )
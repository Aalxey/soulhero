import discord

from discord.ext import commands
from discord import app_commands

from bot.database.repositories.player_repository import PlayerRepository
from bot.services.channel_service import ChannelService

from bot.story.arrival import get_arrival_embed
from bot.views.arrival_view import ArrivalView


class Start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="start",
        description="Begin your journey as a Soul Bearer."
    )
    async def start(self, interaction: discord.Interaction):

        try:

            # -----------------------------
            # Player
            # -----------------------------
            player = PlayerRepository.get_by_discord_id(
                str(interaction.user.id)
            )

            if player is None:

                player = PlayerRepository.create_player(
                    discord_id=str(interaction.user.id),
                    username=interaction.user.name
                )

                print(f"🌑 New Wanderer: {player.username}")

            else:

                print(f"⚔ Welcome back: {player.username}")

            # -----------------------------
            # Create / Get Chamber
            # -----------------------------
            bot_member = interaction.guild.get_member(
                self.bot.user.id
            )

            channel = await ChannelService.get_or_create_awakening_chamber(
                guild=interaction.guild,
                member=interaction.user,
                bot_member=bot_member
            )

            # -----------------------------
            # Send Arrival
            # -----------------------------
            arrival_embed = get_arrival_embed()

            await channel.send(
                embed=arrival_embed,
                view=ArrivalView()
            )

            # -----------------------------
            # Notify Player
            # -----------------------------
            await interaction.response.send_message(
                (
                    "🜂 **The Forgotten Ruins have opened before you.**\n\n"
                    "A quiet whisper beckons from within.\n\n"
                    f"Your path awaits in <#{channel.id}>."
                ),
                ephemeral=True
            )

        except Exception as e:

            print("ERROR:", repr(e))

            if not interaction.response.is_done():

                await interaction.response.send_message(
                    f"An error occurred:\n```{e}```",
                    ephemeral=True
                )


async def setup(bot):
    await bot.add_cog(Start(bot))
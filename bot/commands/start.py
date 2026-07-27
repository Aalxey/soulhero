import discord
from bot.story.prologue import get_prologue_page
from bot.views.prologue_view import PrologueView
from discord.ext import commands
from discord import app_commands
from bot.database.repositories.player_repository import PlayerRepository
from bot.services.channel_service import ChannelService


class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
    name="start",
    description="Begin your journey as a Soul Bearer."
    )
    async def start(self, interaction: discord.Interaction):
        try:
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

            bot_member = interaction.guild.get_member(self.bot.user.id)

            channel = await ChannelService.get_or_create_awakening_chamber(
                guild=interaction.guild,
                member=interaction.user,
                bot_member=bot_member
            )

            await channel.send("🜂 The Forgotten Ruins awaken...")

            embed = get_prologue_page(1)

            await channel.send(
                embed=embed,
                view=PrologueView()
            )

            await interaction.response.send_message(
                f"🜂 **The Soul Core has answered your call.**\n\n"
                f"Your awakening awaits within {channel}.",
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
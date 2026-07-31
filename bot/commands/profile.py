import discord

from discord.ext import commands
from discord import app_commands

from bot.services.player_service import PlayerService
from bot.services.profile_service import ProfileService


class Profile(commands.Cog):

    def __init__(
        self,
        bot
    ):

        self.bot = bot


    @app_commands.command(
        name="profile",
        description="View your own or another player's Soul Profile."
    )
    async def profile(

        self,

        interaction: discord.Interaction,

        member: discord.Member = None

    ):

        # ---------------------------------
        # Only usable inside Soul Chamber
        # ---------------------------------

        if not interaction.channel.name.startswith(
            "soul-chamber-"
        ):

            await interaction.response.send_message(

                (
                    "🏛 This command can only be used inside your "
                    "**Soul Chamber**."
                ),

                ephemeral=True

            )

            return


        # ---------------------------------
        # Default to yourself
        # ---------------------------------

        if member is None:

            member = interaction.user


        player = PlayerService.get_player(

            str(member.id)

        )


        if player is None:

            if member.id == interaction.user.id:

                await interaction.response.send_message(

                    (
                        "🌑 You have not yet begun your journey.\n\n"
                        "Use **/start** to awaken your soul."
                    ),

                    ephemeral=True

                )

            else:

                await interaction.response.send_message(

                    (
                        f"🌑 {member.display_name} has not yet awakened "
                        "their soul."
                    ),

                    ephemeral=True

                )

            return


        embed = ProfileService.build_profile(

            player

        )


        await interaction.response.send_message(

            embed=embed,

            ephemeral=True

        )


async def setup(bot):

    await bot.add_cog(

        Profile(bot)

    )
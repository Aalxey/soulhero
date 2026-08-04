import discord
import traceback

from discord.ext import commands
from discord import app_commands

from bot.services.player_service import PlayerService
from bot.gateway.journey_gateway import JourneyGateway


class Start(commands.Cog):

    def __init__(
        self,
        bot
    ):

        self.bot = bot


    @app_commands.command(
        name="start",
        description="Resume your journey in Soul World."
    )
    async def start(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.defer(
            ephemeral=True
        )

        try:

            discord_id = str(
                interaction.user.id
            )


            # ---------------------------------
            # Load Player
            # ---------------------------------

            player = PlayerService.get_player(
                discord_id
            )


            # ---------------------------------
            # New Wanderer
            # ---------------------------------

            if player is None:

                player = PlayerService.create_player(

                    discord_id,

                    interaction.user.name

                )


                print(
                    f"🌑 New Wanderer: {player.username}"
                )


            else:

                print(
                    f"⚔ Returning soul: {player.username}"
                )


            # ---------------------------------
            # Continue Journey
            # ---------------------------------

            print("🚪 ENTERING JOURNEY GATEWAY")
            await JourneyGateway.resume(

                interaction,

                player,

                self.bot

            )
            print("🚪 JOURNEY GATEWAY FINISHED")


        except Exception as e:
            traceback.print_exc()
            print(
                "START ERROR:",
                repr(e)
            )

            await interaction.followup.send(

                f"An error occurred:\n```{e}```",

                ephemeral=True

            )



async def setup(bot):

    await bot.add_cog(

        Start(bot)

    )
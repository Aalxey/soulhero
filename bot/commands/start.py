import discord

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

        try:

            discord_id = str(
                interaction.user.id
            )


            # ---------------------------------
            # Load / Create Player
            # ---------------------------------

            player = PlayerService.get_player(
                discord_id
            )


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
            # Journey Gateway
            # ---------------------------------

            await JourneyGateway.resume(

                interaction,

                player,

                self.bot

            )


        except Exception as e:

            print(
                "START ERROR:",
                repr(e)
            )


            if not interaction.response.is_done():

                await interaction.response.send_message(

                    f"An error occurred:\n```{e}```",

                    ephemeral=True

                )



async def setup(bot):

    await bot.add_cog(
        Start(bot)
    )
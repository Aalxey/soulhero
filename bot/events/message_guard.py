import discord

from discord.ext import commands

from bot.services.player_service import PlayerService
from bot.utils.constants import JourneyState


class MessageGuard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return


        if message.guild is None:
            return


        player = PlayerService.get_player(
            message.author.id
        )


        if player is None:
            return


        if (
            player.journey_state
            == JourneyState.OATHBOUND.value
        ):
            return


        if not message.channel.name.startswith(
            "forgotten-ruins-"
        ):
            return


        try:
            await message.delete()

        except (
            discord.Forbidden,
            discord.NotFound
        ):
            pass
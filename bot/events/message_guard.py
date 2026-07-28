import discord

from discord.ext import commands

from bot.services.player_service import PlayerService
from bot.utils.constants import JourneyState


class MessageGuard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        # Ignore bots
        if message.author.bot:
            return

        # Ignore DMs
        if message.guild is None:
            return

        player = PlayerService.get_player(
            message.author.id
        )

        if player is None:
            return

        # Only protect players inside the ruins
        if player.journey_state == JourneyState.OATHBOUND:
            return

        channel_name = (
            f"forgotten-ruins-{str(message.author.id)[-4:]}"
        )

        if message.channel.name != channel_name:
            return

        # Delete anything the player types
        try:
            await message.delete()

        except discord.Forbidden:
            pass

        except discord.NotFound:
            pass
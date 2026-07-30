import discord

from bot.engine.scene import Scene
from bot.story.sleeping_hall import get_sleeping_hall_embed
from bot.views.sleeping_hall_view import SleepingHallView


class SleepingHallScene(Scene):
    """
    Hall of Sleeping Heroes.

    Responsibilities:
        - Introduce the Hall.
        - Explain the permanence of the player's choice.
        - Hand control over to SleepingHallView.

    This Scene NEVER:
        - Selects Heroes
        - Updates SQL
        - Forms Oaths
        - Changes JourneyState
    """

    @property
    def scene_name(self) -> str:

        return "SLEEPING_HALL"

    def build_embed(self) -> discord.Embed:

        return get_sleeping_hall_embed()

    def build_view(self):

        return SleepingHallView(

            player_id=int(
                self.player.discord_id
            )

        )
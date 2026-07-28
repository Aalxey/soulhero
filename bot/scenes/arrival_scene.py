import discord

from bot.engine.scene import Scene

from bot.story.arrival import get_arrival_embed
from bot.views.arrival_view import ArrivalView


class ArrivalScene(Scene):

    @property
    def scene_name(self):

        return "ARRIVAL"

    def build_embed(self):

        return get_arrival_embed()

    def build_view(self):

        return ArrivalView(

            player_id=int(
                self.player.discord_id
            )

        )
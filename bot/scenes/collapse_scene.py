import discord

from bot.engine.scene import Scene
from bot.views.ruins_collapse_view import RuinsCollapseView


class CollapseScene(Scene):

    @property
    def scene_name(self):

        return "COLLAPSE"

    def build_embed(self):

        return discord.Embed(

            title="🌋 The Final Trial",

            description=(

                "The air inside the Forgotten Ruins shifts...\n\n"

                "Ancient stones begin to tremble.\n\n"

                "The ancient seal stands before you.\n\n"

                "One final action remains."

            ),

            color=discord.Color.dark_red()

        )

    def build_view(self):

        return RuinsCollapseView(

            player=self.player,

            hero=self.hero

        )
import discord

from bot.engine.scene import Scene

from bot.story.welcome_story import get_welcome_story
from bot.views.welcome_view import WelcomeView


class WelcomeScene(Scene):

    @property
    def scene_name(self):

        return "WELCOME"

    def build_embed(self):

        return discord.Embed(

            title="🌒 The Final Trial",

            description=get_welcome_story(

                self.hero

            ),

            color=discord.Color.dark_purple()

        )

    def build_view(self):

        return WelcomeView(

            hero=self.hero,

            player_id=int(
                self.player.discord_id
            )

        )
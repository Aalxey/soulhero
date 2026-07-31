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

            title="🌑 Welcome to Soul World",

            description=get_welcome_story(

                self.hero

            ),

            color=discord.Color.dark_purple()

        )


    def build_view(self):

        return WelcomeView(

            player=self.player,

            hero=self.hero

        )
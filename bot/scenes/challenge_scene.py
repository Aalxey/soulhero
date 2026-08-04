import discord

from bot.engine.scene import Scene
from bot.views.challenge_view import ChallengeView


class ChallengeScene(Scene):

    def __init__(
        self,
        challenger,
        challenged,
        hero
    ):

        super().__init__(
            challenger,
            hero
        )

        self.challenged = challenged


    @property
    def scene_name(self):

        return "DUEL_CHALLENGE"



    def build_embed(self):

        challenger_name = self.player.username

        hero_name = self.hero["name"]


        embed = discord.Embed(

            title="📜 Duel Challenge",

            description=(

                "A black raven lands before you and drops "
                "a sealed scroll at your feet.\n\n"

                "The crimson seal breaks on its own...\n\n"

                f"**{challenger_name}**, Bearer of **{hero_name}**, "
                "has challenged you to a duel.\n\n"

                "\"Will your soul answer the call?\"\n\n"

                "⏳ **This challenge will disappear in 120 seconds.**"

            ),

            color=discord.Color.dark_red()

        )


        if self.hero.get("image"):

            embed.set_thumbnail(

                url=self.hero["image"]

            )


        embed.set_footer(

            text="The Ravens of Judgement await your decision."

        )


        return embed



    def build_view(self):

        return ChallengeView(

            challenger=self.player,

            challenged=self.challenged,

            hero=self.hero

        )
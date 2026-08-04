import discord

from bot.engine.scene import Scene
from bot.views.oath_ceremony_view import OathCeremonyView


class OathScene(Scene):

    @property
    def scene_name(self):
        return "OATH"

    def build_embed(self):

        embed = discord.Embed(

            title="⚔ Form Oath",

            description=(

                "You are about to form an eternal bond "
                f"with **{self.hero['name']}**.\n\n"

                "⚠ **This decision is permanent.**\n\n"

                "Once your oath is formed, this Hero "
                "will remain beside you throughout "
                "your journey.\n\n"

                "Are you certain?"

            ),

            color=discord.Color.gold()

        )

        if self.hero.get("image"):
            embed.set_thumbnail(url=self.hero["image"])

        embed.set_footer(
            text="The oath cannot be undone."
        )

        return embed

    def build_view(self):

        return OathCeremonyView(

            hero=self.hero,

            player_id=int(self.player.discord_id)

        )
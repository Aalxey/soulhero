import discord

from bot.engine.scene import Scene


class SoulChamberScene(Scene):
    """
    Scene shown when a player first enters
    their permanent Soul Chamber.

    This scene is responsible ONLY for:
    - Building the welcome embed.
    - Returning the view.

    It NEVER:
    - Creates channels
    - Deletes channels
    - Updates SQL
    - Decides progression
    """

    @property
    def scene_name(self) -> str:
        return "SOUL_CHAMBER"

    def build_embed(self) -> discord.Embed:

        hero_name = (
            self.hero["name"]
            if self.hero is not None
            else "your Hero"
        )

        embed = discord.Embed(

            title="🌑 Welcome Home",

            description=(

                "The Forgotten Ruins have fallen silent.\n\n"

                "The oath between you and "
                f"**{hero_name}** has been acknowledged.\n\n"

                "This chamber now belongs to you.\n\n"

                "Within these walls your Hero shall grow.\n"
                "Within these walls your victories shall be remembered.\n"
                "Within these walls your journey shall continue.\n\n"

                "Beyond this sanctuary lies **Soul World**.\n\n"

                "*Whenever your journey becomes difficult...*\n"
                "*this place shall always welcome you back.*"

            ),

            color=discord.Color.dark_purple()

        )

        embed.set_footer(

            text="Soul Chamber • A place only your soul may enter."

        )

        return embed

    def build_view(self) -> discord.ui.View | None:
        """
        The Soul Chamber currently has no buttons.

        Commands such as:
        - /profile
        - /inventory
        - /hero

        will naturally be used inside this channel
        in future updates.
        """

        return None
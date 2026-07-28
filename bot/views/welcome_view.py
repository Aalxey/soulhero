import discord

from bot.story.welcome_story import get_welcome_story
from bot.views.ruins_collapse_view import RuinsCollapseView


class WelcomeView(discord.ui.View):

    def __init__(self, hero):

        super().__init__(
            timeout=None
        )

        self.hero = hero



    @discord.ui.button(
        label="🌑 Continue",
        style=discord.ButtonStyle.primary
    )
    async def continue_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        embed = discord.Embed(

            title="🌋 The Final Trial",

            description=(

                "The air inside the ruins changes...\n\n"

                "Ancient stones begin to tremble.\n\n"

                "The seal protecting this place "
                "is weakening.\n\n"

                "One final step remains."

            ),

            color=discord.Color.dark_purple()

        )


        await interaction.response.edit_message(

            embed=embed,

            view=RuinsCollapseView(
                self.hero
            )

        )
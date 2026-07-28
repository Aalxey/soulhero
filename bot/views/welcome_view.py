import discord


from bot.views.ruins_collapse_view import RuinsCollapseView


class WelcomeView(discord.ui.View):

    def __init__(
        self,
        hero,
        player_id
    ):

        super().__init__(
            timeout=None
        )

        self.hero = hero
        self.player_id = player_id



    @discord.ui.button(
        label="🌑 Continue",
        style=discord.ButtonStyle.primary
    )
    async def continue_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        # Prevent another player using this journey button

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "This journey does not belong to your soul.",
                ephemeral=True
            )

            return



        embed = discord.Embed(

            title="🌋 The Final Trial",

            description=(

                "The air inside the Forgotten Ruins shifts...\n\n"

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
                self.hero,
                self.player_id
            )

        )
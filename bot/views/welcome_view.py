import discord


class WelcomeView(discord.ui.View):

    def __init__(
        self,
        player,
        hero
    ):

        super().__init__(
            timeout=None
        )

        self.player = player
        self.hero = hero


    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if str(interaction.user.id) != self.player.discord_id:

            await interaction.response.send_message(

                "🌑 This chamber does not belong to your soul.",

                ephemeral=True

            )

            return False

        return True


    @discord.ui.button(
        label="⚔ Begin Your Journey",
        style=discord.ButtonStyle.success
    )
    async def begin_journey(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.edit_message(

            content=None,

            embed=None,

            view=None

        )

        await interaction.followup.send(

            (
                "⚔ **The doors of your Soul Chamber slowly open...**\n\n"

                "Beyond them lies **Soul World**.\n\n"

                "May your legend be remembered."

            ),

            ephemeral=True

        )
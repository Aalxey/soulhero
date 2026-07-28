import discord

from bot.services.player_service import PlayerService


class RuinsCollapseView(discord.ui.View):

    def __init__(self, hero):

        super().__init__(
            timeout=None
        )

        self.hero = hero



    @discord.ui.button(
        label="🌋 Break the Ancient Seal",
        style=discord.ButtonStyle.danger
    )
    async def collapse_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        player = PlayerService.collapse_ruins(
            interaction.user.id
        )


        if player is None:

            await interaction.response.send_message(

                "The ruins cannot recognize your soul.",

                ephemeral=True

            )

            return



        embed = discord.Embed(

            title="🌋 The Ruins Collapse",

            description=(

                "The ancient walls begin to break apart.\n\n"

                "Dust fills the forgotten halls.\n\n"

                f"**{self.hero['name']}** stands beside you "
                "as the final seal shatters.\n\n"

                "The path forward has opened.\n\n"

                "⚔ Your oath has been recognized.\n\n"

                "You are now **OATHBOUND**."

            ),

            color=discord.Color.red()

        )


        await interaction.response.edit_message(

            embed=embed,

            view=None

        )
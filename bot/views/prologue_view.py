import discord


class PrologueView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
    label="Next ▶",
    style=discord.ButtonStyle.primary
    )
    async def next_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="📜 Soul Hero",
            description="**Prologue: The Fracture of Worlds**",
            color=discord.Color.gold()
        )

        embed.add_field(
            name="Page 2",
            value=(
                "Far beyond the understanding of ordinary beings...\n\n"
                "A mysterious observer watched over the endless flow of time.\n\n"
                "**???**"
            ),
        inline=False
        )

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )
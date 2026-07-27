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
        await interaction.response.send_message(
            "📖 Next page coming soon...",
            ephemeral=True
        )
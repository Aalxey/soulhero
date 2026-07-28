import discord

from bot.story.soul_core import get_soul_core_embed


class SoulCoreView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

        self.answer_button = discord.ui.Button(
            label="🜂 Answer the Call",
            style=discord.ButtonStyle.success
        )

        self.answer_button.callback = self.answer_callback

        self.add_item(self.answer_button)

    async def answer_callback(
        self,
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            "🌌 The Resonance Ceremony will begin in the next milestone.",
            ephemeral=True
        )
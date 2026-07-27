import discord
from discord.ext import commands
from discord import app_commands


class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="start",
        description="Begin your journey as a Soul Bearer."
    )
    async def start(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "⚔️ Welcome, Soul Bearer!\n\nYour journey has begun..."
        )


async def setup(bot):
    await bot.add_cog(Start(bot))
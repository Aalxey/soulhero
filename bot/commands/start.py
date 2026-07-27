import discord
from bot.story.prologue import get_prologue_page
from bot.views.prologue_view import PrologueView
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
        embed = get_prologue_page(1)

        await interaction.response.send_message(
            embed=embed,
            view=PrologueView()
        )


async def setup(bot):
    await bot.add_cog(Start(bot))
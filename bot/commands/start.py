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

        embed = discord.Embed(
        title="📜 Soul Hero",
        description="**Prologue: The Fracture of Worlds**",
        color=discord.Color.gold()
    )

        embed.add_field(
        name="The Beginning",
        value=(
            "Far beyond the boundaries of our reality lies the "
            "**Land of Dawn**, a world of legendary heroes.\n\n"
            "One day, a mysterious fracture connected their world "
            "to ours..."
        ),
        inline=False
    )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Start(bot))
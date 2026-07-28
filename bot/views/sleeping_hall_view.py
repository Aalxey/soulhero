import discord
from bot.views.hero_search_modal import HeroSearchModal
from bot.services.hero_service import HeroService
from bot.story.sleeping_hall import get_sleeping_hall_embed


class SleepingHallView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)

        self.heroes = HeroService.get_all_heroes()

        self.current_index = 0

        # Previous Chamber
        self.previous_button = discord.ui.Button(
            label="◀ Previous Chamber",
            style=discord.ButtonStyle.secondary
        )
        self.previous_button.callback = self.previous_callback

        # Seek a Soul
        self.search_button = discord.ui.Button(
            label="🔍 Seek a Soul",
            style=discord.ButtonStyle.primary
        )
        self.search_button.callback = self.search_callback

        # Form an Oath
        self.awaken_button = discord.ui.Button(
            label="✨ Form an Oath",
            style=discord.ButtonStyle.success
        )
        self.awaken_button.callback = self.awaken_callback

        # Next Chamber
        self.next_button = discord.ui.Button(
            label="Next Chamber ▶",
            style=discord.ButtonStyle.secondary
        )
        self.next_button.callback = self.next_callback

        self.add_item(self.previous_button)
        self.add_item(self.search_button)
        self.add_item(self.awaken_button)
        self.add_item(self.next_button)

        self.update_buttons()

    def get_current_hero(self):
        return self.heroes[self.current_index]

    def update_buttons(self):

        self.previous_button.disabled = (
            self.current_index == 0
        )

        self.next_button.disabled = (
            self.current_index == len(self.heroes) - 1
        )

    async def previous_callback(
        self,
        interaction: discord.Interaction
    ):
        if self.current_index > 0:
            self.current_index -= 1

        self.update_buttons()

        hero = self.get_current_hero()
        embed = get_sleeping_hall_embed(hero)

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    async def next_callback(
        self,
        interaction: discord.Interaction
    ):
        if self.current_index < len(self.heroes) - 1:
            self.current_index += 1

        self.update_buttons()

        hero = self.get_current_hero()
        embed = get_sleeping_hall_embed(hero)

        await interaction.response.edit_message(
            embed=embed,
            view=self
        )

    async def search_callback(
        self,
        interaction: discord.Interaction
    ):
        await interaction.response.send_modal(
            HeroSearchModal(self)
        )

    async def awaken_callback(
        self,
        interaction: discord.Interaction
    ):
        hero = self.get_current_hero()
        await interaction.response.send_message(
            f"✨ {hero['name']} continues to slumber.\n\n"
            "Their soul has not yet answered your call.",
            ephemeral=True
        )
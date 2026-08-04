import discord

from bot.ui.hero_search_modal import HeroSearchModal
from bot.services.hero_service import HeroService
from bot.services.player_service import PlayerService
from bot.story.sleeping_hall import get_sleeping_hall_embed
from bot.views.oath_ceremony_view import OathCeremonyView


class SleepingHallView(discord.ui.View):

    def __init__(
        self,
        player_id: int
    ):

        super().__init__(
            timeout=None
        )

        self.player_id = player_id

        self.heroes = HeroService.get_all_heroes()

        self.current_index = 0

        self.started_seeking = True


        # Previous Chamber

        self.previous_button = discord.ui.Button(
            label="◀ Previous Chamber",
            style=discord.ButtonStyle.secondary
        )

        self.previous_button.callback = (
            self.previous_callback
        )


        # Seek Soul

        self.search_button = discord.ui.Button(
            label="🔍 Seek a Soul",
            style=discord.ButtonStyle.primary
        )

        self.search_button.callback = (
            self.search_callback
        )


        # Awaken Soul

        self.awaken_button = discord.ui.Button(
            label="✨ Awaken Soul",
            style=discord.ButtonStyle.success
        )

        self.awaken_button.callback = (
            self.awaken_callback
        )


        # Next Chamber

        self.next_button = discord.ui.Button(
            label="Next Chamber ▶",
            style=discord.ButtonStyle.secondary
        )

        self.next_button.callback = (
            self.next_callback
        )


        self.add_item(
            self.previous_button
        )

        self.add_item(
            self.search_button
        )

        self.add_item(
            self.awaken_button
        )

        self.add_item(
            self.next_button
        )


        self.update_buttons()



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 The Sleeping Hall does not recognise your soul.",
                ephemeral=True
            )

            return False


        return True



    def get_current_hero(self):

        if not self.heroes:

            return None


        return self.heroes[
            self.current_index
        ]



    def update_buttons(self):

        self.previous_button.disabled = (
            self.current_index <= 0
        )


        self.next_button.disabled = (
            self.current_index >= len(self.heroes) - 1
        )


        self.search_button.disabled = False


        self.awaken_button.disabled = False



    async def previous_callback(
        self,
        interaction: discord.Interaction
    ):

        if self.current_index > 0:

            self.current_index -= 1


        self.update_buttons()


        hero = self.get_current_hero()


        await interaction.response.edit_message(

            embed=get_sleeping_hall_embed(
                hero
            ),

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


        await interaction.response.edit_message(

            embed=get_sleeping_hall_embed(
                hero
            ),

            view=self

        )



    async def search_callback(
        self,
        interaction: discord.Interaction
    ):


        await interaction.response.send_modal(

            HeroSearchModal(
                self
            )

        )



    async def awaken_callback(
        self,
        interaction: discord.Interaction
    ):


        hero = self.get_current_hero()


        if hero is None:


            await interaction.response.send_message(

                "❌ No sleeping Hero found.",

                ephemeral=True

            )

            return



        # =====================================
        # SAVE HERO BOND
        # =====================================

        player = PlayerService.assign_hero(

            self.player_id,

            hero["id"]

        )


        if player is None:


            await interaction.response.send_message(

                "❌ The Soul Core could not bind this Hero.",

                ephemeral=True

            )

            return



        print(
            f"⚔ Hero bonded: {hero['name']} -> {self.player_id}"
        )



        embed = discord.Embed(

            title=f"✨ {hero['name']} Awakens",

            description=(

                "The Hall trembles...\n\n"

                f"The sleeping soul of **{hero['name']}** "
                "begins to stir.\n\n"

                "\"After countless years of silence...\"\n\n"

                "\"Who dares call my name?\""

            ),

            color=discord.Color.gold()

        )



        view = OathCeremonyView(

            hero,

            self.player_id

        )


        await interaction.response.edit_message(

            embed=embed,

            view=view

        )
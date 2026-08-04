import discord

from bot.services.hero_service import HeroService
from bot.story.sleeping_hall import get_sleeping_hall_embed


class HeroSearchModal(discord.ui.Modal):

    def __init__(
        self,
        hall_view
    ):

        super().__init__(
            title="Seek a Sleeping Soul"
        )

        self.hall_view = hall_view


        self.hero_name = discord.ui.TextInput(

            label="Hero Name",

            placeholder="Example: Alucard",

            required=True,

            max_length=40

        )


        self.add_item(
            self.hero_name
        )



    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        try:

            print(
                f"🔍 Hero search: {self.hero_name.value}"
            )


            hero = HeroService.find_hero_by_name(

                self.hero_name.value

            )


            if hero is None:


                await interaction.response.send_message(

                    "❌ No sleeping Hero answered that name.",

                    ephemeral=True

                )

                return



            print(
                f"✨ Hero found: {hero['name']}"
            )



            index = HeroService.get_hero_index(

                hero["name"]

            )


            if index is None:

                await interaction.response.send_message(

                    "⚠ Hero exists but index could not be found.",

                    ephemeral=True

                )

                return



            self.hall_view.current_index = index


            self.hall_view.started_seeking = True


            self.hall_view.update_buttons()



            embed = get_sleeping_hall_embed(

                hero

            )



            await interaction.response.edit_message(

                embed=embed,

                view=self.hall_view

            )


            print(
                "✅ Sleeping Hall updated"
            )



        except Exception as e:


            print(
                "❌ HERO SEARCH ERROR:",
                repr(e)
            )


            if not interaction.response.is_done():

                await interaction.response.send_message(

                    f"Search failed:\n```{e}```",

                    ephemeral=True

                )
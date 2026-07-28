import discord

from bot.services.hero_service import HeroService
from bot.story.sleeping_hall import get_sleeping_hall_embed


class HeroSearchModal(discord.ui.Modal):

    def __init__(self, hall_view):

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


        self.add_item(self.hero_name)



    async def on_submit(
        self,
        interaction: discord.Interaction
    ):


        # Tell Discord:
        # "I received your request, wait for the result"

        await interaction.response.defer()



        try:

            hero = HeroService.find_hero_by_name(
                self.hero_name.value
            )


            if hero is None:

                await interaction.followup.send(

                    "❌ No sleeping Hero answered that name.",

                    ephemeral=True

                )

                return



            index = HeroService.get_hero_index(
                hero["name"]
            )


            if index is None:

                await interaction.followup.send(

                    "⚠️ The soul was found, but the chamber cannot be located.",

                    ephemeral=True

                )

                return



            # Move Hall to found hero

            self.hall_view.current_index = index


            self.hall_view.update_buttons()



            embed = get_sleeping_hall_embed(
                hero
            )



            await interaction.edit_original_response(

                embed=embed,

                view=self.hall_view

            )



        except Exception as error:


            print(
                "HERO SEARCH ERROR:",
                error
            )


            await interaction.followup.send(

                "⚠️ The Soul Hall encountered an error.",

                ephemeral=True

            )
import discord

from bot.views.sleeping_hall_view import SleepingHallView
from bot.story.sleeping_hall import get_sleeping_hall_embed


class SoulCoreView(discord.ui.View):

    def __init__(
        self,
        player_id: int
    ):

        super().__init__(
            timeout=None
        )

        self.player_id = int(player_id)


        self.answer_button = discord.ui.Button(

            label="🜂 Answer the Call",

            style=discord.ButtonStyle.success,

            custom_id="soul_core_answer"

        )


        self.answer_button.callback = (
            self.answer_callback
        )


        self.add_item(
            self.answer_button
        )



    # ------------------------------------------
    # Security Check
    # ------------------------------------------

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(

                "🌑 The Soul Core rejects your presence.",

                ephemeral=True

            )

            return False


        return True



    # ------------------------------------------
    # Answer The Call
    # ------------------------------------------

    async def answer_callback(
        self,
        interaction: discord.Interaction
    ):

        print(
            "🜂 Answer button pressed:",
            interaction.user.id
        )


        # Respond immediately to Discord
        await interaction.response.defer()


        print(
            "✅ Interaction deferred"
        )


        try:

            # Create Sleeping Hall

            view = SleepingHallView(

                player_id=self.player_id

            )


            print(
                "✅ SleepingHallView created"
            )


            # Get current hero

            hero = view.get_current_hero()


            print(
                "🦸 Current hero:",
                hero
            )


            # Build embed

            embed = get_sleeping_hall_embed(

                hero

            )


            print(
                "📜 Sleeping Hall embed created"
            )


            # Update original message

            await interaction.edit_original_response(

                embed=embed,

                view=view

            )


            print(
                "✅ Sleeping Hall loaded"
            )


        except Exception as e:


            print(

                "❌ ANSWER BUTTON ERROR:",

                repr(e)

            )


            await interaction.followup.send(

                f"Error:\n```{e}```",

                ephemeral=True

            )
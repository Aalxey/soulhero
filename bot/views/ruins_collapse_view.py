import asyncio

import discord

from bot.engine.checkpoint_manager import CheckpointManager
from bot.services.channel_service import ChannelService


class RuinsCollapseView(discord.ui.View):

    def __init__(
        self,
        hero,
        player_id
    ):

        super().__init__(
            timeout=None
        )

        self.hero = hero
        self.player_id = player_id



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(

                "🌑 This journey does not belong to your soul.",

                ephemeral=True

            )

            return False


        return True



    @discord.ui.button(
        label="🌋 Break the Ancient Seal",
        style=discord.ButtonStyle.danger
    )
    async def collapse_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        player = CheckpointManager.collapse_ruins(

            interaction.user.id

        )


        if player is None:


            await interaction.response.send_message(

                "The ruins cannot recognize your soul.",

                ephemeral=True

            )


            return



        embed = discord.Embed(

            title="🌋 The Ruins Collapse",

            description=(

                "The ancient walls begin to break apart.\n\n"

                "Dust fills the forgotten halls.\n\n"

                f"**{self.hero['name']}** stands beside you "
                "as the final seal shatters.\n\n"

                "The path forward has opened.\n\n"

                "⚔ Your oath has been recognized.\n\n"

                "You are now **OATHBOUND**.\n\n"

                "━━━━━━━━━━━━━━━━━━━━━━\n\n"

                "The Forgotten Ruins will fade away in 10 seconds..."

            ),

            color=discord.Color.red()

        )



        await interaction.response.edit_message(

            embed=embed,

            view=None

        )



        # Disable the button permanently

        self.clear_items()



        # Wait before removing the temporary world

        await asyncio.sleep(10)



        try:

            await ChannelService.collapse_ruins_channel(

                interaction.channel

            )


        except Exception as e:

            print(

                "RUINS COLLAPSE ERROR:",

                repr(e)

            )
import asyncio
import discord

from bot.services.player_service import PlayerService
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



    @discord.ui.button(
        label="🌋 Break the Ancient Seal",
        style=discord.ButtonStyle.danger
    )
    async def collapse_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        # ----------------------------
        # Ownership Check
        # ----------------------------

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(

                "🌑 This journey does not belong to your soul.",

                ephemeral=True

            )

            return



        # ----------------------------
        # Collapse Ruins
        # ----------------------------

        player = PlayerService.collapse_ruins(

            interaction.user.id

        )


        if player is None:

            await interaction.response.send_message(

                "The ruins cannot recognize your soul.",

                ephemeral=True

            )

            return



        embed = discord.Embed(

            title="🌋 The Forgotten Ruins Collapse",

            description=(

                "The ancient walls begin to crumble.\n\n"

                "Dust fills the forgotten halls.\n\n"

                f"**{self.hero['name']}** walks beside you as the final seal shatters.\n\n"

                "The Forgotten Ruins have fulfilled their purpose.\n\n"

                "⚔ Your oath has been acknowledged.\n\n"

                "You are now **OATHBOUND**.\n\n"

                "*The ruins will disappear in a few moments...*"

            ),

            color=discord.Color.red()

        )


        await interaction.response.edit_message(

            embed=embed,

            view=None

        )



        # ----------------------------
        # Let player read the ending
        # ----------------------------

        await asyncio.sleep(8)



        # ----------------------------
        # Delete Forgotten Ruins
        # ----------------------------

        await ChannelService.delete_awakening_chamber(

            interaction.guild,

            interaction.user

        )
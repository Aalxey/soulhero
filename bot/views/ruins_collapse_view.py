import asyncio

import discord

from bot.engine.scene_manager import SceneManager

from bot.scenes.welcome_scene import WelcomeScene

from bot.services.player_service import PlayerService
from bot.services.channel_service import ChannelService
from bot.services.soul_chamber_service import SoulChamberService


class RuinsCollapseView(discord.ui.View):

    def __init__(
        self,
        player,
        hero
    ):

        super().__init__(
            timeout=None
        )

        self.player = player
        self.hero = hero



    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if str(interaction.user.id) != self.player.discord_id:

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


        # ---------------------------------
        # Update Player Progression
        # OATH_COMPLETE -> OATHBOUND
        # ---------------------------------

        player = PlayerService.collapse_ruins(

            str(interaction.user.id)

        )


        if player is None:


            await interaction.response.send_message(

                "The ruins cannot recognize your soul.",

                ephemeral=True

            )

            return



        # ---------------------------------
        # Create Permanent Soul Chamber
        # ---------------------------------

        bot_member = interaction.guild.get_member(

            interaction.client.user.id

        )


        chamber = await SoulChamberService.get_or_create(

            guild=interaction.guild,

            member=interaction.user,

            bot_member=bot_member

        )



        # ---------------------------------
        # Ruins Collapse Message
        # ---------------------------------

        embed = discord.Embed(

            title="🌋 The Forgotten Ruins Collapse",

            description=(

                "The ancient walls begin to crumble.\n\n"

                "Dust fills the forgotten halls.\n\n"

                f"**{self.hero['name']}** stands beside you "
                "as the final seal shatters.\n\n"

                "A powerful force suddenly engulfs your soul.\n\n"

                "Before you can react, the world around you "
                "begins to disappear.\n\n"

                "You find yourself being pulled toward "
                "an unknown sanctuary...\n\n"

                f"🏛 **Your Soul Chamber awaits in "
                f"{chamber.mention}.**\n\n"

                "The Forgotten Ruins will disappear in "
                "**10 seconds**."

            ),

            color=discord.Color.red()

        )



        await interaction.response.edit_message(

            embed=embed,

            view=None

        )



        # ---------------------------------
        # Enter Soul Chamber
        # ---------------------------------

        scene = WelcomeScene(

            player,

            self.hero

        )


        await SceneManager.send(

            chamber,

            scene

        )
        print(
            "WELCOME SENT TO:",
            chamber.name
        )



        # Disable old button

        self.clear_items()



        # ---------------------------------
        # Destroy Temporary Ruins
        # ---------------------------------

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
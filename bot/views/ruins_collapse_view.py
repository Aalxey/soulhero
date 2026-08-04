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

        try:

            print(
                "🌋 Ancient seal breaking:",
                interaction.user.id
            )

            # ---------------------------------
            # OATH_COMPLETE -> COLLAPSE
            # ---------------------------------

            player = PlayerService.start_collapse(

                str(interaction.user.id)

            )

            if player is None:

                await interaction.response.send_message(

                    "The ruins cannot recognize your soul.",

                    ephemeral=True

                )

                return

            # ---------------------------------
            # CREATE SOUL CHAMBER
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
            # COLLAPSE -> OATHBOUND
            # ---------------------------------

            player = PlayerService.become_oathbound(

                str(interaction.user.id)

            )

            # ---------------------------------
            # COLLAPSE MESSAGE
            # ---------------------------------

            embed = discord.Embed(

                title="🌋 The Forgotten Ruins Collapse",

                description=(

                    "The ancient walls begin to crumble...\n\n"

                    "Dust fills the forgotten halls.\n\n"

                    f"**{self.hero['name']}** stands beside you "
                    "as the final seal shatters.\n\n"

                    "A powerful force surrounds your soul.\n\n"

                    "The Forgotten Ruins were never your destination.\n\n"

                    "They were only the beginning.\n\n"

                    f"🏛 Your true sanctuary awaits in "
                    f"{chamber.mention}.\n\n"

                    "The ruins will disappear in "
                    "**10 seconds**."

                ),

                color=discord.Color.red()

            )

            await interaction.response.edit_message(

                embed=embed,

                view=None

            )

            # ---------------------------------
            # SEND WELCOME SCENE
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

                "✅ Welcome scene sent:",

                chamber.name

            )

            self.clear_items()

            # ---------------------------------
            # REMOVE OLD RUINS CHANNEL
            # ---------------------------------

            await asyncio.sleep(10)

            try:

                await ChannelService.collapse_ruins_channel(

                    interaction.channel

                )

                print(

                    "✅ Ruins destroyed"

                )

            except Exception as e:

                print(

                    "RUINS COLLAPSE ERROR:",

                    repr(e)

                )

        except Exception:

            import traceback

            print("\n" + "=" * 60)
            print("❌ COLLAPSE BUTTON ERROR")
            print("=" * 60)
            traceback.print_exc()
            print("=" * 60 + "\n")

            try:

                if not interaction.response.is_done():

                    await interaction.response.send_message(

                        "Something went wrong.",

                        ephemeral=True

                    )

                else:

                    await interaction.followup.send(

                        "Something went wrong.",

                        ephemeral=True

                    )

            except Exception:

                pass
import traceback

import discord

from bot.engine.scene_manager import SceneManager
from bot.scenes.collapse_scene import CollapseScene
from bot.services.player_service import PlayerService
from bot.story.oath_dialogue import get_oath_dialogue
from bot.utils.constants import JourneyState


class OathCeremonyView(discord.ui.View):

    def __init__(
        self,
        hero,
        player_id: int
    ):

        super().__init__(
            timeout=None
        )
        print("OathCeremonyView created")

        self.hero = hero
        self.player_id = player_id

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        if interaction.user.id != self.player_id:

            await interaction.response.send_message(
                "🌑 This oath does not belong to your soul.",
                ephemeral=True
            )

            return False

        return True

    @discord.ui.button(
        label="⚔ Accept the Oath",
        style=discord.ButtonStyle.success
    )
    async def accept_oath(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        try:

            print("========== ACCEPT OATH ==========")

            await interaction.response.defer()

            print("1. Interaction deferred")

            player = PlayerService.get_player(
                self.player_id
            )

            print("2. Player:", player)

            if player is None:

                await interaction.followup.send(
                    "The Soul Core cannot find your existence.",
                    ephemeral=True
                )

                return

            print("3. Hero ID:", player.hero_id)

            if player.hero_id is None:

                await interaction.followup.send(
                    "No sleeping soul has answered your call yet.",
                    ephemeral=True
                )

                return

            print("4. Journey:", player.journey_state)

            if player.journey_state == JourneyState.OATH_COMPLETE:

                await interaction.followup.send(
                    "Your oath has already been formed.",
                    ephemeral=True
                )

                return

            # Complete oath
            player = PlayerService.complete_oath(
                self.player_id
            )

            print("5. Oath completed")

            dialogue = get_oath_dialogue(
                self.hero
            )

            embed = discord.Embed(

                title=f"⚔ Oath Formed — {self.hero['name']}",

                description=dialogue["complete"],

                color=discord.Color.gold()

            )

            embed.set_footer(
                text="Your destiny has only begun..."
            )

            print("6. Editing oath message")

            await interaction.edit_original_response(

                embed=embed,

                view=None

            )

            print("7. Oath message edited")

            scene = CollapseScene(

                player,

                self.hero

            )

            print("8. Sending Welcome Scene")

            await SceneManager.send(

                interaction.channel,

                scene

            )

            print("9. Welcome Scene sent")

        except Exception:

            print("===== OATH CEREMONY ERROR =====")

            traceback.print_exc()
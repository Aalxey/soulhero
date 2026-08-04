import discord

from bot.views.attack_view import AttackView

from bot.battle.engine.battle_engine import BattleEngine

from bot.battle.services.battle_refresh_service import BattleRefreshService


class BattleView(discord.ui.View):
    """
    Main battle controls.

    Responsibilities:

    ✓ Open Attack Menu
    ✓ Execute Guard
    ✓ Execute Surrender

    Never:

    ✗ Calculate damage
    ✗ Change HP
    ✗ Decide winner
    ✗ Build embeds
    """

    def __init__(
        self,
        battle
    ):

        super().__init__(
            timeout=None
        )

        self.battle = battle


    # -------------------------------------------------

    def is_player_turn(
        self,
        interaction: discord.Interaction
    ):

        return (
            str(interaction.user.id)
            ==
            str(self.battle.turn)
        )


    # -------------------------------------------------

    @discord.ui.button(
        label="⚔ Attack",
        style=discord.ButtonStyle.primary
    )
    async def attack(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        # -----------------------------
        # Turn Check
        # -----------------------------

        if not self.is_player_turn(interaction):

            await interaction.response.send_message(

                "⚔ It is not your turn.",

                ephemeral=True

            )

            return


        # -----------------------------
        # Open Attack Menu
        # -----------------------------

        # await interaction.response.send_message(

        #     "Choose your skill.",

        #     view=AttackView(

        #         self.battle,

        #         str(interaction.user.id)

        #     ),

        #     ephemeral=True

        # )


    # -------------------------------------------------

    @discord.ui.button(
        label="🛡 Guard",
        style=discord.ButtonStyle.secondary
    )
    async def guard(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        # -----------------------------
        # Turn Check
        # -----------------------------

        if not self.is_player_turn(interaction):

            await interaction.response.send_message(

                "🛡 It is not your turn.",

                ephemeral=True

            )

            return


        # -----------------------------
        # Acknowledge Button
        # -----------------------------

        await interaction.response.defer()


        # -----------------------------
        # Execute Guard
        # -----------------------------

        result = BattleEngine.guard(

            self.battle,

            str(interaction.user.id)

        )


        # -----------------------------
        # Refresh Battle Scene
        # -----------------------------

        await BattleRefreshService.refresh(

            interaction,

            self.battle,

            result

        )


        # -----------------------------
        # Private Message
        # -----------------------------

        await interaction.followup.send(

            "🛡 You entered guard stance.",

            ephemeral=True

        )


    # -------------------------------------------------

    @discord.ui.button(
        label="🏳 Surrender",
        style=discord.ButtonStyle.danger
    )
    async def surrender(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        # -----------------------------
        # Turn Check
        # -----------------------------

        if not self.is_player_turn(interaction):

            await interaction.response.send_message(

                "🏳 It is not your turn.",

                ephemeral=True

            )

            return


        # -----------------------------
        # Acknowledge Button
        # -----------------------------

        await interaction.response.defer()


        # -----------------------------
        # Execute Surrender
        # -----------------------------

        result = BattleEngine.surrender(

            self.battle,

            str(interaction.user.id)

        )


        # -----------------------------
        # Refresh Battle Scene
        # -----------------------------

        await BattleRefreshService.refresh(

            interaction,

            self.battle,

            result

        )


        # -----------------------------
        # Private Message
        # -----------------------------

        await interaction.followup.send(

            "🏳 You surrendered the battle.",

            ephemeral=True

        )
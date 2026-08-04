import discord

from bot.services.hero_memory_service import HeroMemoryService

from bot.battle.engine.battle_engine import BattleEngine

from bot.battle.services.battle_refresh_service import BattleRefreshService


class AttackView(discord.ui.View):
    """
    Ephemeral attack menu.

    This view belongs to the player who
    pressed the Attack button.

    Responsibilities:

        - Display hero skills
        - Execute selected skill
        - Refresh battle after action

    Does NOT:

        - Calculate damage
        - Modify HP
        - Decide winner
    """

    def __init__(
        self,
        battle,
        player_id: str
    ):

        super().__init__(
            timeout=60
        )

        self.battle = battle

        self.player_id = str(player_id)

        self.build_buttons()


    # -------------------------------------------------
    # Build Skill Buttons
    # -------------------------------------------------

    def build_buttons(self):

        player = self.battle.current_player()

        if player is None:
            return


        hero_id = player.hero_id


        slots = [

            "basic_attack",

            "skill_1",

            "skill_2",

            "skill_3"

        ]


        for slot in slots:

            skill = HeroMemoryService.get_skill(

                hero_id,

                slot

            )


            if skill is None:
                continue


            button = discord.ui.Button(

                label=skill["true_name"],

                style=self.get_style(slot),

                custom_id=slot

            )


            button.callback = self.skill_pressed


            self.add_item(button)


        back = discord.ui.Button(

            label="⬅ Back",

            style=discord.ButtonStyle.danger,

            row=1

        )


        back.callback = self.back_pressed


        self.add_item(back)


    # -------------------------------------------------

    @staticmethod
    def get_style(
        slot
    ):

        if slot == "basic_attack":

            return discord.ButtonStyle.primary


        return discord.ButtonStyle.secondary


    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def is_owner(
        self,
        interaction: discord.Interaction
    ):

        return (

            str(interaction.user.id)

            ==

            self.player_id

        )


    def is_turn(self):

        return (

            str(self.battle.turn)

            ==

            self.player_id

        )


    # -------------------------------------------------
    # Skill Button
    # -------------------------------------------------

    async def skill_pressed(
        self,
        interaction: discord.Interaction
    ):


        # -----------------------------
        # Owner Check
        # -----------------------------

        if not self.is_owner(interaction):

            await interaction.response.send_message(

                "This is not your attack menu.",

                ephemeral=True

            )

            return


        # -----------------------------
        # Turn Check
        # -----------------------------

        if not self.is_turn():

            await interaction.response.send_message(

                "It is no longer your turn.",

                ephemeral=True

            )

            return


        skill_slot = interaction.data["custom_id"]


        # -----------------------------
        # Acknowledge Interaction
        # -----------------------------

        await interaction.response.defer()


        # -----------------------------
        # Execute Attack
        # -----------------------------

        result = BattleEngine.attack(

            self.battle,

            self.player_id,

            skill_slot

        )


        # -----------------------------
        # Update Battle Message
        # -----------------------------

        await BattleRefreshService.refresh(

            interaction,

            self.battle,

            result

        )


        # -----------------------------
        # Close Menu
        # -----------------------------

        self.disable_buttons()

        self.stop()



    # -------------------------------------------------
    # Disable UI
    # -------------------------------------------------

    def disable_buttons(self):

        for item in self.children:

            item.disabled = True



    # -------------------------------------------------
    # Back Button
    # -------------------------------------------------

    async def back_pressed(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.defer()

        self.disable_buttons()

        self.stop()
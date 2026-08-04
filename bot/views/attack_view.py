import traceback

import discord
import asyncio

from bot.services.hero_memory_service import HeroMemoryService
from bot.battle.engine.battle_engine import BattleEngine
from bot.battle.services.battle_refresh_service import BattleRefreshService


class AttackView(discord.ui.View):

    def __init__(
        self,
        battle,
        player_id: str
    ):

        super().__init__(
            timeout=None
        )


        self.battle = battle

        self.player_id = str(player_id)


        print("\n")
        print("=" * 60)
        print("⚔ ATTACK VIEW CREATED")
        print("Player ID:", self.player_id)
        print("Battle ID:", id(self.battle))
        print("Battle Finished:", getattr(self.battle, "finished", False))
        print("Current Turn:", self.battle.turn)
        print("=" * 60)



        # -----------------------------------
        # Do not create buttons after victory
        # -----------------------------------

        if getattr(self.battle, "finished", False):

            print(
                "🏆 Battle already finished."
            )

            return



        self.build_buttons()



    # =================================================
    # BUILD BUTTONS
    # =================================================

    def build_buttons(self):

        print(
            "⚔ BUILDING ATTACK BUTTONS"
        )


        player = self.battle.current_player()


        if player is None:

            print(
                "❌ CURRENT PLAYER NONE"
            )

            return



        print(
            "Current player:",
            player.username
        )


        print(
            "Hero ID:",
            player.hero_id
        )



        skills = [

            "basic_attack",

            "skill_1",

            "skill_2",

            "skill_3"

        ]



        for slot in skills:


            print(
                "Loading skill:",
                slot
            )


            skill = HeroMemoryService.get_skill(

                player.hero_id,

                slot

            )


            if skill is None:

                print(
                    "❌ Missing skill:",
                    slot
                )

                continue



            print(
                "✅ Skill:",
                skill["true_name"]
            )



            button = discord.ui.Button(

                label=skill["true_name"],

                style=self.get_style(slot),

                custom_id=f"attack_{slot}"

            )


            button.callback = self.skill_pressed


            self.add_item(button)




        back = discord.ui.Button(

            label="⬅ Back",

            style=discord.ButtonStyle.danger,

            custom_id="attack_back",

            row=1

        )


        back.callback = self.back_pressed


        self.add_item(back)



        print(
            "✅ ATTACK BUTTONS READY"
        )



    # =================================================
    # STYLE
    # =================================================

    @staticmethod
    def get_style(slot):

        if slot == "basic_attack":

            return discord.ButtonStyle.primary


        return discord.ButtonStyle.secondary



    # =================================================
    # OWNER CHECK
    # =================================================

    def is_owner(
        self,
        interaction
    ):


        result = (

            str(interaction.user.id)

            ==

            self.player_id

        )


        print(
            "OWNER CHECK:",
            result
        )


        return result



    # =================================================
    # TURN CHECK
    # =================================================

    def is_turn(self):

        result = (

            str(self.battle.turn)

            ==

            self.player_id

        )


        print(
            "TURN CHECK:",
            result
        )

        print(
            "Expected:",
            self.player_id
        )

        print(
            "Current:",
            self.battle.turn
        )


        return result



    # =================================================
    # SKILL CLICK
    # =================================================

    async def skill_pressed(
        self,
        interaction: discord.Interaction
    ):


        print("\n")
        print("=" * 60)
        print("⚔ SKILL CLICK")
        print("=" * 60)


        try:


            # -----------------------------------
            # Battle already finished protection
            # -----------------------------------

            if getattr(
                self.battle,
                "finished",
                False
            ):


                print(
                    "🏆 Battle already finished"
                )


                await interaction.response.send_message(

                    "⚔ This battle has already ended.",

                    ephemeral=True

                )


                return



            print(
                "User:",
                interaction.user
            )


            print(
                "Data:",
                interaction.data
            )



            if not self.is_owner(interaction):


                print(
                    "❌ Wrong player"
                )


                await interaction.response.send_message(

                    "This attack menu belongs to another soul.",

                    ephemeral=True

                )


                return



            print(
                "✅ OWNER VERIFIED"
            )



            if not self.is_turn():


                print(
                    "❌ Wrong turn"
                )


                await interaction.response.send_message(

                    "It is not your turn.",

                    ephemeral=True

                )


                return



            print(
                "✅ TURN VERIFIED"
            )



            skill_id = interaction.data["custom_id"]


            print(
                "Button:",
                skill_id
            )



            skill_slot = skill_id.replace(

                "attack_",

                ""

            )


            print(
                "Skill:",
                skill_slot
            )



            await interaction.response.defer()



            print(
                "✅ Deferred"
            )



            result = BattleEngine.attack(

                self.battle,

                self.player_id,

                skill_slot

            )



            print(
                "RESULT:"
            )


            print(
                result.__dict__
            )



            # -----------------------------------
            # Refresh battle
            # -----------------------------------

            await BattleRefreshService.refresh(

                interaction,

                self.battle,

                result

            )

            if result.finished:

                await asyncio.sleep(15)

                from bot.services.battle_cleanup_service import BattleCleanupService

                await BattleCleanupService.delete_channel(
                    self.battle
                )


            print(
                "✅ REFRESH COMPLETE"
            )



            # -----------------------------------
            # Close old menu
            # -----------------------------------

            self.disable_buttons()

            self.stop()



            print(
                "✅ ATTACK VIEW CLOSED"
            )



        except Exception:


            print("\n")
            print("=" * 60)
            print("❌ ATTACK VIEW ERROR")
            print("=" * 60)


            traceback.print_exc()


            print("=" * 60)




    # =================================================
    # DISABLE
    # =================================================

    def disable_buttons(self):


        print(
            "DISABLING BUTTONS"
        )


        for child in self.children:

            child.disabled = True




    # =================================================
    # BACK
    # =================================================

    async def back_pressed(
        self,
        interaction
    ):


        print(
            "⬅ BACK CLICKED"
        )


        await interaction.response.defer()


        self.disable_buttons()

        self.stop()


        print(
            "BACK COMPLETE"
        )
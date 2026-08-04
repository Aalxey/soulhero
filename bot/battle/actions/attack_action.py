from bot.battle.battle_result import BattleResult

from bot.battle.services.luck_service import LuckService

from bot.services.hero_memory_service import HeroMemoryService

from bot.services.damage_service import DamageService


class AttackAction:
    """
    Handles offensive battle actions.

    This class ONLY handles combat logic.

    It does NOT:
        - Discord
        - embeds
        - messages
        - database
    """

    @staticmethod
    def execute(
        battle,
        attacker_id: str,
        skill_slot: str
    ):

        print("\n========== ATTACK ACTION ==========")

        result = BattleResult()


        # ---------------------------------
        # Turn Check
        # ---------------------------------

        if str(battle.turn) != str(attacker_id):

            print("❌ Not player's turn")

            result.action = "attack"

            return result



        # ---------------------------------
        # Load States
        # ---------------------------------

        attacker = battle.state_of(

            attacker_id

        )

        defender = battle.opponent_state(

            attacker_id

        )


        print(
            "Attacker:",
            attacker.player.username
        )

        print(
            "Defender:",
            defender.player.username
        )


        # ---------------------------------
        # Load Skill
        # ---------------------------------

        skill = HeroMemoryService.get_skill(

            attacker.hero["id"],

            skill_slot

        )


        print(
            "Skill:",
            skill
        )


        if skill is None:

            print(
                "❌ Skill does not exist"
            )

            result.failed_memory = True

            result.action = "attack"

            return result



        result.skill = skill



        # ---------------------------------
        # Forgotten Skill
        # ---------------------------------

        if skill.get("power") is None:

            print(
                "❓ Forgotten skill"
            )

            result.failed_memory = True

            result.action = "forgotten_skill"

            return result



        # ---------------------------------
        # Cooldown Check
        # ---------------------------------

        if skill_slot != "basic_attack":

            cooldown = attacker.cooldown(

                skill_slot

            )


            print(
                "Cooldown:",
                cooldown
            )


            if cooldown > 0:

                print(
                    "⏳ Skill on cooldown"
                )

                result.action = "cooldown"

                return result



        # ---------------------------------
        # Luck
        # ---------------------------------

        luck_result = LuckService.roll(

            attacker.luck

        )


        result.critical = luck_result.success


        print(
            "Critical:",
            result.critical
        )



        # ---------------------------------
        # Damage
        # ---------------------------------

        damage_result = DamageService.calculate(

            attacker,

            defender,

            skill,

            result.critical

        )


        result.damage = damage_result.damage

        result.damage_type = skill.get(

            "damage_type"

        )


        print(
            "Damage:",
            result.damage
        )


        # ---------------------------------
        # Apply Damage
        # ---------------------------------

        defender.take_damage(

            result.damage

        )


        print(
            "Enemy HP:",
            defender.current_hp
        )



        # ---------------------------------
        # Apply Cooldown
        # ---------------------------------

        if skill_slot != "basic_attack":


            cooldown = skill.get(

                "cooldown",

                0

            )


            attacker.set_cooldown(

                skill_slot,

                cooldown

            )


            print(
                "Cooldown applied:",
                cooldown
            )



        # ---------------------------------
        # Defeat
        # ---------------------------------

        if defender.defeated:


            print(
                "🏆 Enemy defeated"
            )


            result.defeated = True

            result.finished = True

            result.winner = attacker.player



        # ---------------------------------
        # Next Turn
        # ---------------------------------

        if not result.finished:


            battle.next_turn()


            print(
                "Next turn:",
                battle.turn
            )



        result.action = "attack"


        print(
            "========== ATTACK COMPLETE ==========\n"
        )


        return result
from bot.battle.models.battle_result import BattleResult

from bot.battle.services.luck_service import LuckService

from bot.services.hero_memory_service import HeroMemoryService

from bot.services.damage_service import DamageService


class AttackAction:
    """
    Handles every offensive action.

    This class does NOT:
        - handle Discord
        - edit messages
        - create embeds

    It only performs combat logic.
    """


    @staticmethod
    def execute(
        battle,
        attacker_id: str,
        skill_slot: str
    ):

        result = BattleResult()


        # ---------------------------------
        # Check Turn
        # ---------------------------------

        if battle.turn != str(attacker_id):

            result.action = "attack"

            result.finished = False

            return result



        # ---------------------------------
        # Get States
        # ---------------------------------

        attacker = battle.state_of(
            attacker_id
        )

        defender = battle.opponent_state(
            attacker_id
        )



        # ---------------------------------
        # Get Skill
        # ---------------------------------

        skill = HeroMemoryService.get_skill(

            attacker.hero["id"],

            skill_slot

        )


        if skill is None:

            result.failed_memory = True

            result.action = "attack"

            return result



        result.skill = skill



        # ---------------------------------
        # Forgotten Skill Check
        # ---------------------------------

        if skill["power"] is None:

            result.failed_memory = True

            result.action = "forgotten_skill"

            return result



        # ---------------------------------
        # Cooldown Check
        # ---------------------------------

        if skill_slot != "basic_attack":

            if attacker.cooldown(skill_slot) > 0:

                result.action = "attack"

                return result



        # ---------------------------------
        # Luck Roll
        # ---------------------------------

        luck_result = LuckService.roll(

            attacker.luck

        )


        result.critical = luck_result.success



        # ---------------------------------
        # Damage Calculation
        # ---------------------------------

        damage_result = DamageService.calculate(

            attacker,

            defender,

            skill,

            result.critical

        )



        result.damage = damage_result.damage

        result.damage_type = skill["damage_type"]



        # ---------------------------------
        # Apply Damage
        # ---------------------------------

        defender.take_damage(

            result.damage

        )



        # ---------------------------------
        # Cooldown
        # ---------------------------------

        if skill_slot != "basic_attack":

            attacker.set_cooldown(

                skill_slot,

                skill["cooldown"]

            )



        # ---------------------------------
        # Defeat
        # ---------------------------------

        if defender.defeated:

            result.defeated = True

            result.finished = True

            result.winner = attacker.player



        # ---------------------------------
        # Next Turn
        # ---------------------------------

        if not result.finished:

            battle.next_turn()



        # ---------------------------------
        # Return Result
        # ---------------------------------

        result.action = "attack"

        return result
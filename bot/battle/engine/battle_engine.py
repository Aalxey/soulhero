from bot.battle.actions.attack_action import AttackAction
from bot.battle.actions.guard_action import GuardAction
from bot.battle.actions.surrender_action import SurrenderAction


class BattleEngine:
    """
    Central entry point for every battle action.

    BattleEngine NEVER:

        - Builds Discord embeds
        - Sends Discord messages
        - Updates the database
        - Gives Resonance
        - Records wins/losses

    It ONLY coordinates gameplay.
    """

    # -------------------------------------------------

    @staticmethod
    def attack(
        battle,
        attacker_id: str,
        skill_slot: str
    ):

        result = AttackAction.execute(

            battle,

            attacker_id,

            skill_slot

        )

        BattleEngine._finalize(

            battle,

            result

        )

        return result

    # -------------------------------------------------

    @staticmethod
    def guard(
        battle,
        player_id: str
    ):

        result = GuardAction.execute(

            battle,

            player_id

        )

        BattleEngine._finalize(

            battle,

            result

        )

        return result

    # -------------------------------------------------

    @staticmethod
    def surrender(
        battle,
        player_id: str
    ):

        result = SurrenderAction.execute(

            battle,

            player_id

        )

        BattleEngine._finalize(

            battle,

            result

        )

        return result

    # -------------------------------------------------

    @staticmethod
    def _finalize(
        battle,
        result
    ):
        """
        Synchronizes the Battle object after an action.

        This method DOES NOT:

            - Record wins
            - Record losses
            - Give Resonance
            - Remove battles

        Those belong to higher-level services.
        """

        if not result.finished:

            return

        battle.finish(

            result.winner

        )
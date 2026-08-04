from bot.battle.battle_result import BattleResult


class GuardAction:
    """
    Handles the Guard action.

    Guard reduces the damage received from
    the next incoming attack.

    After the player is attacked,
    the guard automatically disappears.
    """

    @staticmethod
    def execute(
        battle,
        player_id: str
    ):

        result = BattleResult()

        result.action = "guard"

        # ---------------------------------
        # Turn Check
        # ---------------------------------

        if battle.turn != str(player_id):

            return result

        # ---------------------------------
        # Player
        # ---------------------------------

        player = battle.state_of(
            player_id
        )

        # ---------------------------------
        # Activate Guard
        # ---------------------------------

        player.activate_guard()

        result.guarded = True

        # ---------------------------------
        # End Turn
        # ---------------------------------

        battle.next_turn()

        return result
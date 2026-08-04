from bot.battle.battle_result import BattleResult


class SurrenderAction:
    """
    Instantly ends the battle.

    The opponent becomes the winner.
    """

    @staticmethod
    def execute(
        battle,
        player_id: str
    ):

        result = BattleResult()

        result.action = "surrender"

        # ---------------------------------
        # Player States
        # ---------------------------------

        loser = battle.state_of(
            player_id
        )

        winner = battle.opponent_state(
            player_id
        )

        # ---------------------------------
        # Finish Battle
        # ---------------------------------

        loser.defeated = True

        result.finished = True

        result.defeated = True

        result.winner = winner.player

        battle.finish(
            winner.player
        )

        return result
from bot.database.repositories.player_repository import PlayerRepository
from bot.services.player_service import PlayerService
from bot.services.resonance_service import ResonanceService


class BattleService:
    """
    Handles every battle-related operation.

    Owns:
        - Wins
        - Losses
        - Win Rate

    Does NOT own:
        - Discord UI
        - Battle mechanics
        - Matchmaking
    """

    WIN_RESONANCE_REWARD = 10

    @staticmethod
    def record_win(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        player = PlayerRepository.update(

            player,

            wins=player.wins + 1

        )

        ResonanceService.add_resonance(

            discord_id,

            BattleService.WIN_RESONANCE_REWARD

        )

        return player

    @staticmethod
    def record_loss(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        return PlayerRepository.update(

            player,

            losses=player.losses + 1

        )

    @staticmethod
    def get_wins(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return 0

        return player.wins

    @staticmethod
    def get_losses(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return 0

        return player.losses

    @staticmethod
    def get_stats(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:

            return None

        total = (

            player.wins +

            player.losses

        )

        if total == 0:

            win_rate = 0.0

        else:

            win_rate = round(

                (player.wins / total) * 100,

                2

            )

        return {

            "wins": player.wins,

            "losses": player.losses,

            "total_battles": total,

            "win_rate": win_rate

        }
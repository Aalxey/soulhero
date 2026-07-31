from bot.database.repositories.player_repository import PlayerRepository
from bot.services.player_service import PlayerService


class ResonanceService:
    """
    Handles every Resonance-related operation.

    Resonance represents the player's progression.

    Every gameplay system that rewards progression
    should use this service.
    """

    # Minimum Resonance required for each Bond
    BONDS = (
        (200, "True Oath"),
        (100, "Soul Connection"),
        (50, "Trusted Companion"),
        (25, "Familiar Bond"),
        (10, "First Encounter"),
        (1, "Stranger"),
    )

    @staticmethod
    def get_resonance(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        return player.resonance

    @staticmethod
    def add_resonance(
        discord_id: str,
        amount: int
    ):

        if amount <= 0:
            return None

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        return PlayerRepository.update(

            player,

            resonance=player.resonance + amount

        )

    @staticmethod
    def remove_resonance(
        discord_id: str,
        amount: int
    ):

        if amount <= 0:
            return None

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        new_resonance = max(

            1,

            player.resonance - amount

        )

        return PlayerRepository.update(

            player,

            resonance=new_resonance

        )

    @staticmethod
    def get_bond(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )

        if player is None:
            return None

        resonance = player.resonance

        for minimum, bond in ResonanceService.BONDS:

            if resonance >= minimum:
                return bond

        return "Stranger"
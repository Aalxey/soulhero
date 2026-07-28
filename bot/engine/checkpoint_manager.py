from bot.services.player_service import PlayerService


class CheckpointManager:
    """
    Central bridge between Views and Player progression.

    It does not contain progression rules.
    PlayerService remains the source of truth.

    Responsibilities:
        - Receive checkpoint requests
        - Forward them to PlayerService
    """

    @staticmethod
    def update_state(
        discord_id,
        journey_state
    ):

        return PlayerService.update_state(

            str(discord_id),

            journey_state

        )


    @staticmethod
    def collapse_ruins(
        discord_id
    ):

        return PlayerService.collapse_ruins(

            str(discord_id)

        )
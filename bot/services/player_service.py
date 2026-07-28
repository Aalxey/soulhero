from datetime import datetime

from bot.database.repositories.player_repository import PlayerRepository
from bot.utils.constants import JourneyState

from bot.services.hero_service import HeroService


class PlayerService:


    @staticmethod
    def get_player(
        discord_id: str
    ):

        return PlayerRepository.get_by_discord_id(
            str(discord_id)
        )



    @staticmethod
    def create_player(
        discord_id: str,
        username: str
    ):

        existing_player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if existing_player:

            return existing_player



        return PlayerRepository.create(
            discord_id=str(discord_id),
            username=username
        )



    @staticmethod
    def update_state(
        discord_id: str,
        state
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        return PlayerRepository.update(
            player,
            journey_state=state
        )



    @staticmethod
    def assign_hero(
        discord_id: str,
        hero_id: int
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        # One soul can only bond with one Hero

        if player.hero_id is not None:

            return player



        return PlayerRepository.update(
            player,

            hero_id=hero_id,

            journey_state=JourneyState.HERO_CHOSEN
        )



    @staticmethod
    def complete_oath(
        discord_id: str
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        # Oath requires Hero bond

        if player.hero_id is None:

            return player



        return PlayerRepository.update(
            player,

            journey_state=JourneyState.OATH_COMPLETE
        )



    @staticmethod
    def enter_welcome(
        discord_id: str
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        # Welcome only after oath

        if (
            player.journey_state
            != JourneyState.OATH_COMPLETE
        ):

            return player



        return PlayerRepository.update(
            player,

            journey_state=JourneyState.WELCOME
        )



    @staticmethod
    def collapse_ruins(
        discord_id: str
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        # Ruins collapse only after welcome

        if (
            player.journey_state
            != JourneyState.WELCOME
        ):

            return player



        return PlayerRepository.update(
            player,

            journey_state=JourneyState.OATHBOUND,

            oathbound_date=datetime.utcnow()
        )



    @staticmethod
    def get_hero_id(
        discord_id: str
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return None



        return player.hero_id



    @staticmethod
    def is_oathbound(
        discord_id: str
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if player is None:

            return False



        return (
            player.journey_state
            == JourneyState.OATHBOUND
        )

    @staticmethod
    def get_player_hero(
        discord_id: str
    ):

        player = PlayerService.get_player(
            discord_id
        )


        if player is None:
            return None


        if player.hero_id is None:
            return None


        return HeroService.get_hero_by_id(
            player.hero_id
        )
from bot.services.hero_service import HeroService
from bot.utils.constants import JourneyState


class JourneyService:
    """
    Responsible ONLY for deciding where a player's journey should continue.

    No Discord code.
    No SQL code.
    No Views.
    """

    @staticmethod
    def get_scene(player):

        if player is None:
            return "ARRIVAL"

        state = player.journey_state

        if state == JourneyState.WANDERER:
            return "ARRIVAL"

        if state == JourneyState.AWAKENING:
            return "SLEEPING_HALL"

        if state == JourneyState.HERO_CHOSEN:
            return "OATH"

        if state == JourneyState.OATH_COMPLETE:
            return "WELCOME"

        if state == JourneyState.WELCOME:
            return "COLLAPSE"

        if state == JourneyState.OATHBOUND:
            return "SOUL_WORLD"

        return "ARRIVAL"

    @staticmethod
    def get_player_hero(player):
        """
        Returns the player's hero dictionary from heroes.json.
        """

        if player is None:
            return None

        if player.hero_id is None:
            return None

        for hero in HeroService.get_all_heroes():

            if hero["id"] == player.hero_id:
                return hero

        return None
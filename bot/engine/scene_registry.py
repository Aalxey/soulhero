from bot.utils.constants import JourneyState


class SceneRegistry:
    """
    Registry that maps a player's JourneyState
    to a Scene name.

    SceneManager will later use this to
    instantiate the correct Scene.
    """

    _registry = {

        JourneyState.WANDERER:
            "ARRIVAL",

        JourneyState.AWAKENING:
            "SLEEPING_HALL",

        JourneyState.HERO_CHOSEN:
            "OATH",

        JourneyState.OATH_COMPLETE:
            "WELCOME",

        JourneyState.WELCOME:
            "COLLAPSE",

        JourneyState.OATHBOUND:
            "SOUL_WORLD",

    }

    @classmethod
    def get_scene_name(
        cls,
        journey_state
    ):

        return cls._registry.get(
            journey_state,
            "ARRIVAL"
        )
from bot.utils.constants import JourneyState

from bot.scenes.arrival_scene import ArrivalScene
from bot.scenes.welcome_scene import WelcomeScene
from bot.scenes.collapse_scene import CollapseScene


class SceneRegistry:

    _registry = {

        JourneyState.WANDERER:
            ArrivalScene,


        JourneyState.OATH_COMPLETE:
            WelcomeScene,


        JourneyState.WELCOME:
            CollapseScene,

    }


    @classmethod
    def get_scene(

        cls,

        journey_state

    ):

        return cls._registry.get(

            journey_state

        )
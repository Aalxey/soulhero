from enum import Enum


class JourneyState(str, Enum):

    WANDERER = "WANDERER"

    AWAKENING = "AWAKENING"

    HERO_CHOSEN = "HERO_CHOSEN"

    OATH_COMPLETE = "OATH_COMPLETE"

    COLLAPSE = "COLLAPSE"

    WELCOME = "WELCOME"

    OATHBOUND = "OATHBOUND"



    @property
    def has_hero(self):

        return self in (
            JourneyState.HERO_CHOSEN,
            JourneyState.OATH_COMPLETE,
            JourneyState.COLLAPSE,
            JourneyState.WELCOME,
            JourneyState.OATHBOUND
        )



    @property
    def oath_complete(self):

        return self in (
            JourneyState.OATH_COMPLETE,
            JourneyState.COLLAPSE,
            JourneyState.WELCOME,
            JourneyState.OATHBOUND
        )



    @property
    def in_ruins(self):

        return self in (
            JourneyState.AWAKENING,
            JourneyState.HERO_CHOSEN,
            JourneyState.OATH_COMPLETE,
            JourneyState.COLLAPSE
        )
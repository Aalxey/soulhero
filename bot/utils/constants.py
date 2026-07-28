from enum import Enum


class JourneyState(str, Enum):

    WANDERER = "WANDERER"

    AWAKENING = "AWAKENING"

    HERO_CHOSEN = "HERO_CHOSEN"

    OATH_COMPLETE = "OATH_COMPLETE"

    WELCOME = "WELCOME"

    OATHBOUND = "OATHBOUND"
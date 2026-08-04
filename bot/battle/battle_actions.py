from enum import Enum


class BattleAction(str, Enum):

    # -------------------------
    # Attack Menu
    # -------------------------

    BASIC_ATTACK = "BASIC_ATTACK"

    FORGOTTEN_SKILL_1 = "FORGOTTEN_SKILL_1"

    FORGOTTEN_SKILL_2 = "FORGOTTEN_SKILL_2"

    FORGOTTEN_SKILL_3 = "FORGOTTEN_SKILL_3"

    # -------------------------
    # Battle Menu
    # -------------------------

    GUARD = "GUARD"

    SURRENDER = "SURRENDER"
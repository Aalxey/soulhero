from bot.services.hero_service import HeroService


class HeroMemoryService:
    """
    Controls what skills are visible to players.

    Heroes always contain their real skills inside heroes.json.

    This service decides whether the player sees:

        ❓ Forgotten Skill

    or

        Night Raid

    depending on whether that hero has been awakened
    by the developers.
    """

    # ------------------------------------------
    # Heroes whose memories have awakened.
    #
    # Example:
    #
    # {1, 5, 18}
    #
    # means hero ids:
    #   1
    #   5
    #   18
    #
    # reveal every skill.
    # ------------------------------------------

    AWAKENED_HEROES = set()

    # ------------------------------------------

    FORGOTTEN_NAMES = {
        "skill_1": "❓ Forgotten Skill I",
        "skill_2": "❓ Forgotten Skill II",
        "skill_3": "❓ Forgotten Skill III"
    }

    # ------------------------------------------

    FORGOTTEN_DESCRIPTION = (
        "The hero struggles to remember this forgotten memory..."
    )

    # ------------------------------------------

    @classmethod
    def awaken_hero(
        cls,
        hero_id: int
    ):

        cls.AWAKENED_HEROES.add(hero_id)

    # ------------------------------------------

    @classmethod
    def seal_hero(
        cls,
        hero_id: int
    ):

        cls.AWAKENED_HEROES.discard(hero_id)

    # ------------------------------------------

    @classmethod
    def hero_is_awakened(
        cls,
        hero_id: int
    ):

        return hero_id in cls.AWAKENED_HEROES

    # ------------------------------------------

    @classmethod
    def get_skill(
        cls,
        hero_id: int,
        slot: str
    ):

        hero = HeroService.get_hero_by_id(hero_id)

        if hero is None:
            return None

        for skill in hero["skills"]:

            if skill["slot"] != slot:
                continue

            # Basic attack is always visible

            if slot == "basic_attack":
                return skill

            # Hero awakened

            if cls.hero_is_awakened(hero_id):
                return skill

            # Hidden

            return {

                "slot": slot,

                "true_name": cls.FORGOTTEN_NAMES[slot],

                "description": cls.FORGOTTEN_DESCRIPTION,

                "damage_type": None,

                "power": None,

                "cooldown": None

            }

        return None
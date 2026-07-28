import json
from pathlib import Path
from random import choice


class HeroService:

    DATA_PATH = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "heroes.json"
    )

    _heroes = None

    @classmethod
    def load_heroes(cls):

        if cls._heroes is None:

            with open(
                cls.DATA_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                cls._heroes = json.load(file)

        return cls._heroes

    # -------------------------------------

    @classmethod
    def get_all_heroes(cls):

        return cls.load_heroes()

    # -------------------------------------

    @classmethod
    def get_hero_by_id(
        cls,
        hero_id: int
    ):

        for hero in cls.get_all_heroes():

            if hero["id"] == hero_id:
                return hero

        return None

    # -------------------------------------

    @classmethod
    def find_hero_by_name(
        cls,
        hero_name: str
    ):

        hero_name = hero_name.lower().strip()

        for hero in cls.get_all_heroes():

            if hero["name"].lower() == hero_name:
                return hero

        return None

    # -------------------------------------

    @classmethod
    def get_hero_index(
        cls,
        hero_name: str
    ):

        hero_name = hero_name.lower().strip()

        for index, hero in enumerate(
            cls.get_all_heroes()
        ):

            if hero["name"].lower() == hero_name:
                return index

        return None

    # -------------------------------------

    @classmethod
    def hero_exists(
        cls,
        hero_id: int
    ):

        return cls.get_hero_by_id(hero_id) is not None

    # -------------------------------------

    @classmethod
    def random_hero(cls):

        return choice(
            cls.get_all_heroes()
        )
import json
from pathlib import Path


class HeroService:

    DATA_PATH = (
        Path(__file__).resolve()
        .parents[2]
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

    @classmethod
    def get_all_heroes(cls):
        return cls.load_heroes()

    @classmethod
    def get_by_id(cls, hero_id):

        heroes = cls.load_heroes()

        for hero in heroes:

            if hero["id"] == hero_id:
                return hero

        return None

    @classmethod
    def get_by_name(cls, name):

        heroes = cls.load_heroes()

        for hero in heroes:

            if hero["name"].lower() == name.lower():
                return hero

        return None

    @classmethod
    def search(cls, query):

        heroes = cls.load_heroes()

        query = query.lower()

        return [

            hero

            for hero in heroes

            if query in hero["name"].lower()

        ]
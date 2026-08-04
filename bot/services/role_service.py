import json
from pathlib import Path


class RoleService:

    DATA_PATH = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "roles.json"
    )

    _roles = None

    @classmethod
    def load_roles(cls):

        if cls._roles is None:

            with open(
                cls.DATA_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                cls._roles = json.load(file)

        return cls._roles

    # -----------------------------------------

    @classmethod
    def get_role(
        cls,
        role_name: str
    ):

        return cls.load_roles().get(role_name)

    # -----------------------------------------

    @classmethod
    def role_exists(
        cls,
        role_name: str
    ):

        return role_name in cls.load_roles()

    # -----------------------------------------

    @classmethod
    def get_stat(
        cls,
        role_name: str,
        stat: str
    ):

        role = cls.get_role(role_name)

        if role is None:

            return None

        return role.get(stat)
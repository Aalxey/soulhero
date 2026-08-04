from bot.battle.battle import Battle


class BattleManager:
    """
    Keeps track of every active battle.

    This manager ONLY stores active battles.

    It does NOT:
        - Create Discord channels
        - Send embeds
        - Handle buttons
        - Update SQL
    """

    _battles = {}

    @classmethod
    def create(
        cls,
        player_one,
        player_two
    ):

        battle = Battle(

            player_one,

            player_two

        )

        cls._battles[battle.id] = battle

        return battle

    @classmethod
    def get(
        cls,
        battle_id: str
    ):

        return cls._battles.get(

            battle_id

        )

    @classmethod
    def get_by_player(
        cls,
        discord_id: str
    ):

        for battle in cls._battles.values():

            if battle.contains(

                str(discord_id)

            ):

                return battle

        return None

    @classmethod
    def is_in_battle(
        cls,
        discord_id: str
    ):

        return (

            cls.get_by_player(

                discord_id

            )

            is not None

        )

    @classmethod
    def remove(
        cls,
        battle_id: str
    ):

        cls._battles.pop(

            battle_id,

            None

        )

    @classmethod
    def remove_player(
        cls,
        discord_id: str
    ):

        battle = cls.get_by_player(

            discord_id

        )

        if battle is None:

            return

        cls.remove(

            battle.id

        )

    @classmethod
    def all(cls):

        return list(

            cls._battles.values()

        )
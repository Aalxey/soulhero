from bot.services.hero_service import HeroService
from bot.services.role_service import RoleService


class StatService:
    """
    Calculates a player's final battle stats.

    Formula

    Base Role Stats
        +
    Resonance Growth
        +
    Manual Bonus Stats
        +
    Hero Stat Modifier

    =
    Final Battle Stats
    """

    @staticmethod
    def get_stats(player):

        hero = HeroService.get_hero_by_id(
            player.hero_id
        )

        if hero is None:

            raise ValueError(

                f"Hero {player.hero_id} does not exist."

            )

        role = RoleService.get_role(

            hero["role"]

        )

        if role is None:

            raise ValueError(

                f"Role '{hero['role']}' does not exist."

            )

        base = role["base"]

        growth = role["growth"]

        resonance = max(

            1,

            player.resonance

        )

        level = resonance - 1

        stats = {

            "max_hp":

                base["max_hp"]

                +

                (

                    growth["max_hp"]

                    * level

                )

                +

                player.allocated_hp,

            "attack":

                base["attack"]

                +

                (

                    growth["attack"]

                    * level

                )

                +

                player.allocated_attack,

            "defense":

                base["defense"]

                +

                (

                    growth["defense"]

                    * level

                )

                +

                player.allocated_defense,

            "speed":

                base["speed"]

                +

                (

                    growth["speed"]

                    * level

                )

                +

                player.allocated_speed,

            "luck":

                player.luck

        }

        modifier = hero.get(

            "stat_modifier",

            {}

        )

        for stat, value in modifier.items():

            if stat in stats:

                stats[stat] += value

        return stats
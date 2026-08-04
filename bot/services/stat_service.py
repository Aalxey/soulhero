from bot.services.hero_service import HeroService
from bot.services.role_service import RoleService



class StatService:
    """
    Calculates a player's final battle stats.

    Formula:

        Role Base Stats
              +
        Resonance Growth
              +
        Player Allocated Stats
              +
        Hero Modifier
              +
        Future Bonuses

        =
        Final Battle Stats


    This service NEVER:

        ✗ Changes player data
        ✗ Saves database
        ✗ Handles battle
        ✗ Handles Discord
    """



    @staticmethod
    def get_stats(player):


        # ---------------------------------
        # Get Hero
        # ---------------------------------

        hero = HeroService.get_hero_by_id(

            player.hero_id

        )


        if hero is None:

            raise ValueError(

                f"Hero '{player.hero_id}' does not exist."

            )



        # ---------------------------------
        # Get Role
        # ---------------------------------

        role = RoleService.get_role(

            hero["role"]

        )


        if role is None:

            raise ValueError(

                f"Role '{hero['role']}' does not exist."

            )



        # ---------------------------------
        # Base Data
        # ---------------------------------

        base = role["base"]

        growth = role["growth"]



        # ---------------------------------
        # Resonance Level
        # ---------------------------------

        resonance = max(

            1,

            player.resonance

        )


        level = resonance - 1



        # ---------------------------------
        # Calculate Stats
        # ---------------------------------

        stats = {


            "max_hp":

                base["max_hp"]

                +

                (

                    growth["max_hp"]

                    *

                    level

                )

                +

                getattr(

                    player,

                    "allocated_hp",

                    0

                ),



            "attack":

                base["attack"]

                +

                (

                    growth["attack"]

                    *

                    level

                )

                +

                getattr(

                    player,

                    "allocated_attack",

                    0

                ),



            "defense":

                base["defense"]

                +

                (

                    growth["defense"]

                    *

                    level

                )

                +

                getattr(

                    player,

                    "allocated_defense",

                    0

                ),



            "speed":

                base["speed"]

                +

                (

                    growth["speed"]

                    *

                    level

                )

                +

                getattr(

                    player,

                    "allocated_speed",

                    0

                ),



            "luck":

                getattr(

                    player,

                    "luck",

                    0

                )

        }



        # ---------------------------------
        # Hero Passive Modifier
        # ---------------------------------

        modifier = hero.get(

            "stat_modifier",

            {}

        )



        for stat, value in modifier.items():


            if stat in stats:

                stats[stat] += value



        # ---------------------------------
        # Safety Checks
        # ---------------------------------

        stats["max_hp"] = max(

            1,

            stats["max_hp"]

        )


        stats["attack"] = max(

            1,

            stats["attack"]

        )


        stats["defense"] = max(

            1,

            stats["defense"]

        )


        stats["speed"] = max(

            1,

            stats["speed"]

        )


        stats["luck"] = max(

            0,

            stats["luck"]

        )



        return stats
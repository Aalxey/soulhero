from bot.services.hero_service import HeroService
from bot.services.stat_service import StatService


class BattleState:
    """
    Temporary combat state.

    Exists only during active battle.
    """


    def __init__(
        self,
        player
    ):

        print("\n========== BATTLE STATE CREATE ==========")

        self.player = player


        # -------------------------
        # Hero
        # -------------------------

        self.hero_id = player.hero_id


        self.hero = HeroService.get_hero_by_id(
            player.hero_id
        )


        print(
            "Player:",
            player.username
        )

        print(
            "Hero ID:",
            self.hero_id
        )


        stats = StatService.get_stats(
            player
        )


        print(
            "Stats:",
            stats
        )


        # -------------------------
        # Battle Stats
        # -------------------------

        self.max_hp = stats["max_hp"]

        self.current_hp = self.max_hp


        self.attack = stats["attack"]

        self.defense = stats["defense"]

        self.speed = stats["speed"]

        self.luck = stats["luck"]



        print(
            "HP:",
            self.current_hp
        )

        print(
            "ATK:",
            self.attack
        )

        print(
            "DEF:",
            self.defense
        )


        # -------------------------
        # Battle Flags
        # -------------------------

        self.guarding = False

        self.defeated = False



        # -------------------------
        # Cooldowns
        # -------------------------

        self.cooldowns = {

            "skill_1": 0,

            "skill_2": 0,

            "skill_3": 0

        }



        self.buffs = []

        self.debuffs = []

        self.status_effects = []


        print(
            "========== STATE READY ==========\n"
        )



    # =================================================
    # HP ALIAS
    # =================================================

    @property
    def hp(self):

        return self.current_hp



    @hp.setter
    def hp(
        self,
        value
    ):

        self.current_hp = value



    # =================================================
    # DAMAGE
    # =================================================


    def take_damage(
        self,
        damage:int
    ):

        print(
            "\n========== DAMAGE TAKEN =========="
        )


        print(
            "Before HP:",
            self.current_hp
        )


        if self.defeated:

            print(
                "Already defeated"
            )

            return 0



        old_hp = self.current_hp


        self.current_hp = max(

            0,

            self.current_hp - damage

        )


        actual_damage = old_hp - self.current_hp



        print(
            "Damage:",
            actual_damage
        )


        print(
            "After HP:",
            self.current_hp
        )


        if self.current_hp == 0:


            self.defeated = True


            print(
                "☠ DEFEATED:",
                self.player.username
            )


        print(
            "================================\n"
        )


        return actual_damage



    # =================================================
    # HEAL
    # =================================================


    def heal(
        self,
        amount:int
    ):


        if self.defeated:

            return 0



        old_hp = self.current_hp


        self.current_hp = min(

            self.max_hp,

            self.current_hp + amount

        )


        healed = self.current_hp - old_hp



        print(
            "💚 HEAL:",
            healed
        )


        return healed



    # =================================================
    # GUARD
    # =================================================


    def activate_guard(self):

        self.guarding = True


        print(
            "🛡 Guard:",
            self.player.username
        )



    def remove_guard(self):

        self.guarding = False



    def is_guarding(self):

        return self.guarding



    # =================================================
    # STATUS
    # =================================================


    def is_alive(self):

        return not self.defeated



    # =================================================
    # COOLDOWN
    # =================================================


    def set_cooldown(
        self,
        skill,
        turns
    ):

        self.cooldowns[skill] = turns


        print(
            "Cooldown:",
            skill,
            turns
        )



    def cooldown(
        self,
        skill
    ):

        return self.cooldowns.get(
            skill,
            0
        )



    def reduce_cooldowns(self):

        for skill in self.cooldowns:


            if self.cooldowns[skill] > 0:

                self.cooldowns[skill] -= 1



        print(
            "Cooldowns:",
            self.cooldowns
        )
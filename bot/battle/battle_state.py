from bot.services.hero_service import HeroService
from bot.services.stat_service import StatService


class BattleState:
    """
    Represents one player's temporary state during battle.

    Everything here exists ONLY while a battle is active.

    Nothing in this class is permanently stored.
    """

    def __init__(self, player):

        self.player = player

        self.hero = HeroService.get_hero_by_id(
            player.hero_id
        )

        stats = StatService.get_stats(player)

        # -------------------------
        # Battle Stats
        # -------------------------

        self.max_hp = stats["max_hp"]

        self.current_hp = stats["max_hp"]

        self.attack = stats["attack"]

        self.defense = stats["defense"]

        self.speed = stats["speed"]

        self.luck = stats["luck"]

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

        # -------------------------
        # Future Systems
        # -------------------------

        self.buffs = []

        self.debuffs = []

        self.status_effects = []

    # -------------------------------------------------

    def take_damage(
        self,
        damage: int
    ):

        self.current_hp = max(

            0,

            self.current_hp - damage

        )

        if self.current_hp == 0:

            self.defeated = True

    # -------------------------------------------------

    def heal(
        self,
        amount: int
    ):

        self.current_hp = min(

            self.max_hp,

            self.current_hp + amount

        )

    # -------------------------------------------------

    def activate_guard(self):

        self.guarding = True

    # -------------------------------------------------

    def remove_guard(self):

        self.guarding = False

    # -------------------------------------------------

    def is_guarding(self):

        return self.guarding

    # -------------------------------------------------

    def is_alive(self):

        return not self.defeated

    # -------------------------------------------------

    def set_cooldown(
        self,
        skill: str,
        turns: int
    ):

        self.cooldowns[skill] = turns

    # -------------------------------------------------

    def cooldown(
        self,
        skill: str
    ):

        return self.cooldowns.get(

            skill,

            0

        )

    # -------------------------------------------------

    def reduce_cooldowns(self):

        for skill in self.cooldowns:

            if self.cooldowns[skill] > 0:

                self.cooldowns[skill] -= 1
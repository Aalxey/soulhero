class BattleResult:
    """
    Represents the result of one battle action.

    Every combat action returns one BattleResult.

    The BattleScene reads this object to display
    everything that happened during the turn.
    """

    def __init__(self):

        # -------------------------
        # Action
        # -------------------------

        self.action = None

        self.skill = None

        # -------------------------
        # Damage
        # -------------------------

        self.damage = 0

        self.damage_type = None

        self.critical = False

        self.guarded = False

        self.missed = False

        # -------------------------
        # Forgotten Skills
        # -------------------------

        self.remembered = False

        self.failed_memory = False

        # -------------------------
        # Healing
        # -------------------------

        self.heal = 0

        # -------------------------
        # Status
        # -------------------------

        self.buff_applied = None

        self.debuff_applied = None

        self.status_effect = None

        # -------------------------
        # Battle State
        # -------------------------

        self.defeated = False

        self.winner = None

        self.finished = False

        # -------------------------
        # Future Systems
        # -------------------------

        self.counter_attack = False

        self.life_steal = 0

        self.shield_absorbed = 0

        self.extra_turn = False
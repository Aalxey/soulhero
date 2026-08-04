class DamageResult:
    """
    Result returned by DamageService.

    This object contains everything needed to
    describe an attack.
    """

    def __init__(
        self,
        damage: int,
        critical: bool,
        variation: float,
    ):

        self.damage = damage

        self.critical = critical

        self.variation = variation
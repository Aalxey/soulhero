class LuckResult:
    """
    Represents one luck roll.

    Every random event inside Souls should use
    LuckResult.

    Examples:
        - Critical Hits
        - Hero Memory
        - Treasure Chests
        - Crafting
        - Dungeon Events
        - Rare Drops
    """

    def __init__(self):

        # -------------------------
        # Overall Result
        # -------------------------

        self.success = False

        # -------------------------
        # Dice Information
        # -------------------------

        self.dice_used = 0

        self.successful_dice = 0

        self.failed_dice = 0

        # Every die result
        # Example:
        # [False, False, True]
        self.rolls = []

        # -------------------------
        # Debug / Logging
        # -------------------------

        self.reason = None
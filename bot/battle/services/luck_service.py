import random

from bot.battle.models.luck_result import LuckResult


class LuckService:
    """
    Handles all luck-based events in Souls.

    Used for:
        - Critical hits
        - Forgotten skill awakening
        - Rare rewards
        - Events
        - Future systems
    """


    # -----------------------------------------
    # Determine dice amount from luck
    # -----------------------------------------

    @staticmethod
    def get_dice_count(
        luck: int
    ):

        if luck <= 20:

            return 1

        elif luck <= 40:

            return 2

        elif luck <= 60:

            return 3

        elif luck <= 80:

            return 4

        else:

            return 5



    # -----------------------------------------
    # Roll luck
    # -----------------------------------------

    @staticmethod
    def roll(
        luck: int
    ):

        result = LuckResult()


        print("\n========== LUCK ROLL ==========")

        print(
            "Luck:",
            luck
        )


        # -------------------------
        # Dice Amount
        # -------------------------

        dice_count = LuckService.get_dice_count(
            luck
        )


        result.dice_used = dice_count


        print(
            "Dice used:",
            dice_count
        )


        # -------------------------
        # Roll Dice
        # -------------------------

        for index in range(dice_count):

            roll = random.choice(
                [
                    True,
                    False
                ]
            )


            result.rolls.append(
                roll
            )


            print(
                f"Dice {index + 1}:",
                "SUCCESS" if roll else "FAIL"
            )


            if roll:

                result.successful_dice += 1

            else:

                result.failed_dice += 1



        # -------------------------
        # Final Result
        # -------------------------

        result.success = (

            result.successful_dice > 0

        )


        result.reason = (

            "Luck succeeded"

            if result.success

            else

            "Luck failed"

        )


        print(
            "Success:",
            result.success
        )

        print(
            "Successful:",
            result.successful_dice
        )

        print(
            "Failed:",
            result.failed_dice
        )

        print(
            "==============================\n"
        )


        return result
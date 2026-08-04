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


    @staticmethod
    def roll(
        luck: int
    ):

        result = LuckResult()


        dice_count = LuckService.get_dice_count(
            luck
        )


        result.dice_count = dice_count


        for _ in range(dice_count):

            roll = random.choice(
                [
                    True,
                    False
                ]
            )


            result.results.append(
                roll
            )


            if roll:

                result.success_count += 1

            else:

                result.fail_count += 1


        # One success is enough

        result.success = (
            result.success_count > 0
        )


        return result
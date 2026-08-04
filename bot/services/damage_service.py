import random

from bot.battle.damage_result import DamageResult


class DamageService:
    """
    Calculates battle damage.

    This service NEVER modifies HP.

    It only calculates and returns
    a DamageResult.
    """

    @staticmethod
    def calculate(

        attacker,

        defender,

        skill,

        critical=False

    ):

        # ----------------------------------
        # Stats
        # ----------------------------------

        attack = attacker.attack

        defense = max(

            1,

            defender.defense

        )

        power = skill["power"]

        # ----------------------------------
        # Base Damage
        # ----------------------------------

        base_damage = (

            attack * power

        ) / defense

        # ----------------------------------
        # Random Battle Variation
        # ----------------------------------

        variation = random.uniform(

            0.90,

            1.10

        )

        damage = int(

            base_damage * variation

        )

        # ----------------------------------
        # Critical Hit
        # ----------------------------------

        if critical:

            damage = int(

                damage * 1.5

            )

        # ----------------------------------
        # Guard
        # ----------------------------------

        if defender.guarding:

            damage = int(

                damage * 0.5

            )

        # ----------------------------------
        # Minimum Damage
        # ----------------------------------

        damage = max(

            1,

            damage

        )

        return DamageResult(

            damage=damage,

            critical=critical,

            variation=variation

        )
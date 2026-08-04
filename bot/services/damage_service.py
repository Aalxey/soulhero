import random
import traceback

from bot.battle.damage_result import DamageResult


class DamageService:
    """
    Calculates battle damage.

    This service ONLY calculates damage.

    It does NOT:
        - modify HP
        - decide winner
        - handle Discord
    """


    @staticmethod
    def calculate(
        attacker,
        defender,
        skill,
        critical=False
    ):

        print("\n")
        print("=" * 60)
        print("⚔ DAMAGE CALCULATION START")
        print("=" * 60)


        try:


            # ----------------------------------
            # Debug Objects
            # ----------------------------------

            print(
                "ATTACKER:",
                attacker.player.username
                if hasattr(attacker.player, "username")
                else attacker.player
            )


            print(
                "DEFENDER:",
                defender.player.username
                if hasattr(defender.player, "username")
                else defender.player
            )


            print(
                "SKILL:",
                skill
            )



            # ----------------------------------
            # Read Stats
            # ----------------------------------

            attack = attacker.attack

            defense = max(
                1,
                defender.defense
            )


            power = skill.get(
                "power",
                0
            )



            print(
                "ATTACK STAT:",
                attack
            )


            print(
                "DEFENSE STAT:",
                defense
            )


            print(
                "SKILL POWER:",
                power
            )



            # ----------------------------------
            # Invalid Skill Protection
            # ----------------------------------

            if power is None:


                print(
                    "❌ Skill has no power"
                )


                return DamageResult(

                    damage=0,

                    critical=False,

                    variation=1

                )



            # ----------------------------------
            # Base Damage
            # ----------------------------------

            base_damage = (

                attack * power

            ) / defense



            print(
                "BASE DAMAGE:",
                base_damage
            )



            # ----------------------------------
            # Random Variation
            # ----------------------------------

            variation = random.uniform(

                0.90,

                1.10

            )


            print(
                "DAMAGE VARIATION:",
                variation
            )


            damage = int(

                base_damage * variation

            )



            # ----------------------------------
            # Critical Damage
            # ----------------------------------

            if critical:


                print(
                    "💥 CRITICAL HIT"
                )


                damage = int(

                    damage * 1.5

                )


            else:


                print(
                    "Critical: FALSE"
                )



            # ----------------------------------
            # Guard Reduction
            # ----------------------------------

            if defender.guarding:


                print(
                    "🛡 DEFENDER GUARDING"
                )


                damage = int(

                    damage * 0.5

                )


            else:


                print(
                    "Guard: FALSE"
                )



            # ----------------------------------
            # Minimum Damage
            # ----------------------------------

            damage = max(

                1,

                damage

            )



            print(
                "FINAL DAMAGE:",
                damage
            )



            # ----------------------------------
            # Create Result
            # ----------------------------------

            result = DamageResult(

                damage=damage,

                critical=critical,

                variation=variation

            )


            print(
                "DamageResult created successfully"
            )


            print("=" * 60)
            print("⚔ DAMAGE CALCULATION END")
            print("=" * 60)
            print("\n")


            return result



        except Exception:


            print("\n")
            print("=" * 60)
            print("❌ DAMAGE SERVICE ERROR")
            print("=" * 60)


            traceback.print_exc()


            print("=" * 60)
            print("\n")


            raise
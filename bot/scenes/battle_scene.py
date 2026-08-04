import discord

from bot.views.battle_view import BattleView


class BattleScene:
    """
    Displays the current battle.

    BattleScene is responsible ONLY for presentation.

    It never:

        - Calculates damage
        - Changes HP
        - Decides turns
        - Rolls luck

    Those belong to the battle engine.

    BattleScene simply converts the current battle
    into a Discord Embed + View.
    """

    def __init__(
        self,
        battle,
        result=None
    ):

        self.battle = battle
        self.result = result

    # -------------------------------------------------

    @property
    def scene_name(self):

        return "BATTLE"

    # -------------------------------------------------

    def build_embed(self):

        embed = discord.Embed(
            title="⚔ Battle",
            color=discord.Color.red()
        )

        player_one = self.battle.player_one
        player_two = self.battle.player_two

        state_one = self.battle.player_one_state
        state_two = self.battle.player_two_state

        current_player = self.battle.current_player()

        description = [

            "━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"⚔ **{player_one.username}**",
            f"❤️ {state_one.current_hp}/{state_one.max_hp}",
            "",
            "🆚",
            "",
            f"⚔ **{player_two.username}**",
            f"❤️ {state_two.current_hp}/{state_two.max_hp}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━",
            ""
        ]

        # -----------------------------------------
        # Last Action
        # -----------------------------------------

        if self.result is not None:

            description.extend(

                self._build_action_log()

            )

        # -----------------------------------------
        # Turn
        # -----------------------------------------

        description.extend([

            "",
            f"🎯 **Turn:** {current_player.username}"

        ])

        embed.description = "\n".join(description)

        return embed

    # -------------------------------------------------

    def _build_action_log(self):

        result = self.result

        lines = []

        if result.action == "attack":

            skill_name = (
                result.skill["true_name"]
                if result.skill
                else "Attack"
            )

            lines.append(
                f"⚔ **{skill_name}**"
            )

            if result.failed_memory:

                lines.append(
                    "❓ This memory is still sealed."
                )

                return lines

            if result.missed:

                lines.append(
                    "💨 The attack missed!"
                )

                return lines

            damage = result.damage

            if result.critical:

                lines.append(
                    "💥 **Critical Hit!**"
                )

            lines.append(
                f"🩸 Damage: **{damage}**"
            )

            if result.guarded:

                lines.append(
                    "🛡 Damage Reduced"
                )

            if result.defeated:

                lines.append(
                    "☠ Enemy Defeated!"
                )

        elif result.action == "guard":

            lines.append(
                "🛡 Guard Stance Activated"
            )

        elif result.action == "surrender":

            lines.append(
                "🏳 Player Surrendered"
            )

        return lines

    # -------------------------------------------------

    def build_view(self):

        return BattleView(
            self.battle
        )
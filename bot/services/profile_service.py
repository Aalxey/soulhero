import discord

from bot.services.hero_service import HeroService
from bot.services.resonance_service import ResonanceService
from bot.services.battle_record_service import BattleService


class ProfileService:

    @staticmethod
    def build_profile(player):

        hero = HeroService.get_hero_by_id(
            player.hero_id
        )

        stats = BattleService.get_stats(
            player.discord_id
        )

        bond = ResonanceService.get_bond(
            player.discord_id
        )

        hero_name = (
            hero["name"]
            if hero is not None
            else "None"
        )

        oath_date = (
            player.oathbound_date.strftime("%d %B %Y")
            if player.oathbound_date
            else "Not Yet"
        )

        embed = discord.Embed(

            description=(

                "╔══════════════════════╗\n"
                "       ⚔ **SOUL PROFILE**\n"
                "╚══════════════════════╝\n\n"

                "🌑 **Name**\n"
                f"{player.username}\n\n"

                "⚔ **Hero**\n"
                f"{hero_name}\n\n"

                "✨ **Resonance**\n"
                f"{player.resonance}\n\n"

                "🔗 **Bond**\n"
                f"{bond}\n\n"

                "⚔ **Battles**\n"
                f"{stats['total_battles']}\n\n"

                "🏆 **Victories**\n"
                f"{stats['wins']}\n\n"

                "💀 **Defeats**\n"
                f"{stats['losses']}\n\n"

                "🕯 **Oath Formed**\n"
                f"{oath_date}"

            ),

            color=discord.Color.dark_purple()

        )

        return embed
import discord


def get_arrival_embed() -> discord.Embed:
    embed = discord.Embed(
        title="🜂 The Forgotten Ruins",
        description=(
            "Darkness.\n\n"

            "For a fleeting moment, every sense abandons you.\n\n"

            "The ground beneath your feet gives way...\n\n"

            "...and silence follows.\n\n"

            "As your vision slowly returns, you find yourself lying upon weathered stone.\n\n"

            "Towering pillars, worn by countless ages, surround you.\n\n"

            "The air is heavy with dust, and not a single living soul answers your breath.\n\n"

            "You have fallen into a place long forgotten by the world.\n\n"

            "Drawn by curiosity, you begin searching the ruins for answers.\n\n"

            "At the heart of the ruins stands an ancient stone altar.\n\n"

            "Resting upon it lies a weathered chronicle, untouched by time itself.\n\n"

            "Perhaps its pages hold the truth behind this forgotten place."
        ),
        color=0x5B4B8A
    )

    embed.set_footer(
        text="Every forgotten place remembers a story."
    )

    return embed
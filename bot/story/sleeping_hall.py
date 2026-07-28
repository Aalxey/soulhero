import discord


def get_sleeping_hall_embed(hero):

    embed = discord.Embed(
        title="🏛 Hall of Sleeping Heroes",
        colour=discord.Colour.dark_gold()
    )

    embed.description = (
        "Beyond the Soul Core lies a silent sanctuary.\n\n"

        "Crystal chambers stretch farther than your eyes can follow.\n\n"

        "Within each crystal rests a Hero whose memories were scattered by the Fracture.\n\n"

        "Some dream peacefully.\n"
        "Some still grip invisible weapons.\n"
        "Some quietly wait for the one who will call their name.\n\n"

        "**Before you stands one of those sleeping souls.**"
    )

    embed.add_field(
        name=f"⚔ {hero['name']}",
        value=(
            f"**Role:** {hero['role']}\n\n"

            "The Hero slumbers peacefully within the crystal.\n"

            "Perhaps your voice is the one they have waited to hear."
        ),
        inline=False
    )

    embed.set_footer(
        text="Every Hero waits for an Oathbound."
    )

    return embed
import discord


def get_sleeping_hall_embed(hero=None):

    embed = discord.Embed(
        title="🏛 Hall of Sleeping Heroes",
        colour=discord.Colour.dark_gold()
    )


    if hero is None:

        embed.description = (

            "Rows of crystal chambers stretch into the darkness.\n\n"

            "Within each slumbers a Hero,\n"
            "waiting for the one whose soul resonates with theirs.\n\n"

            "The choice you make today\n"
            "will shape the journey ahead.\n\n"

            "⚠ **An oath, once formed, is eternal.**"

        )

        embed.set_footer(
            text="When you are ready, begin seeking."
        )

        return embed



    # -----------------------------
    # Hero discovered
    # -----------------------------

    embed.title = (
        f"🏛 Sleeping Chamber: {hero['name']}"
    )


    embed.description = (

        f"Within this crystal chamber sleeps **{hero['name']}**.\n\n"

        f"⚔ Role: **{hero['role']}**\n\n"

        "The soul within remains silent...\n"

        "waiting to see if your resonance is worthy."

    )


    if hero.get("biography"):

        embed.add_field(
            name="📖 Memory Fragment",
            value=hero["biography"],
            inline=False
        )


    embed.set_footer(
        text="A sleeping soul awaits your call."
    )


    return embed
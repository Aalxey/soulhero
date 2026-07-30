import discord


def get_sleeping_hall_embed():

    embed = discord.Embed(

        title="🏛 Hall of Sleeping Heroes",

        colour=discord.Colour.dark_gold()

    )

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
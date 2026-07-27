import discord


def get_prologue_page(page: int) -> discord.Embed:
    embed = discord.Embed(
        title="📜 Soul Hero",
        colour=discord.Colour.gold()
    )

    if page == 1:
        embed.description = "**Prologue: The Fracture of Worlds**"

        embed.add_field(
            name="The Beginning",
            value=(
                "Far beyond the boundaries of our reality lies the "
                "**Land of Dawn**, a world of legendary heroes.\n\n"
                "One day, a mysterious fracture connected their world "
                "to ours..."
            ),
            inline=False
        )

    elif page == 2:
        embed.description = "**Prologue: The Fracture of Worlds**"

        embed.add_field(
            name="The Watcher",
            value=(
                "Far beyond the understanding of ordinary beings...\n\n"
                "A mysterious observer watched over the endless flow of time.\n\n"
                "**???**"
            ),
            inline=False
        )

    elif page == 3:
        embed.description = "**Prologue: The Fracture of Worlds**"

        embed.add_field(
            name="The Forgotten Heroes",
            value=(
                "The fracture spread across both worlds.\n\n"
                "One by one, the legendary Heroes were pulled from the "
                "Land of Dawn into an unfamiliar world.\n\n"
                "Their memories faded, their purpose became uncertain, "
                "yet deep within their hearts, a faint light still remained...\n\n"
                "The Soul Core."
            ),
            inline=False
        )

    elif page == 4:
        embed.description = "**Prologue: The Fracture of Worlds**"

        embed.add_field(
            name="A New Beginning",
            value=(
                "The Soul Core has awakened.\n\n"
                "Across the fractured worlds, countless Heroes answered its call.\n\n"
                "Some seek their forgotten past.\n"
                "Some seek the road back home.\n\n"
                "**All seek an Oathbound worthy of walking beside them.**\n\n"
                "Choose the Hero whose heart resonates with yours."
            ),
            inline=False
        )
    return embed
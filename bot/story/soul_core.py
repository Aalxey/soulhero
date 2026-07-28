import discord


def get_soul_core_embed() -> discord.Embed:
    embed = discord.Embed(
        title="🜂 The Soul Core Awakens",
        description=(
            "Silence falls once more.\n\n"

            "The ruins fade into darkness as an ancient light begins to breathe.\n\n"

            "Before you stands the Soul Core—the heart from which countless oaths were once forged.\n\n"

            "It does not speak.\n\n"

            "Yet its presence reaches into your very soul.\n\n"

            "Your resonance travels beyond the veil...\n\n"

            "**And something answers.**"
        ),
        color=0xD8C27A
    )

    embed.set_footer(
        text="Not every soul answers the call."
    )

    return embed
import discord

from config import SOUL_CHAMBER_CATEGORY_ID


class SoulChamberService:
    """
    Responsible ONLY for managing a player's Soul Chamber.

    Responsibilities:
    - Find an existing Soul Chamber.
    - Create one if it does not exist.
    - Return the player's chamber.

    This service NEVER:
    - Sends embeds
    - Sends Discord messages
    - Updates SQL
    - Deletes channels
    - Contains game logic
    """

    @staticmethod
    async def get_or_create(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ) -> discord.TextChannel:

        category = guild.get_channel(
            SOUL_CHAMBER_CATEGORY_ID
        )

        if category is None:
            raise ValueError(
                "Soul Chamber category was not found."
            )

        channel_name = (
            f"soul-chamber-{str(member.id)[-4:]}"
        )

        existing_channel = discord.utils.get(
            category.channels,
            name=channel_name
        )

        if existing_channel is not None:
            return existing_channel

        overwrites = {

            guild.default_role:
                discord.PermissionOverwrite(
                    view_channel=False
                ),

            member:
                discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True,
                    embed_links=True,
                    attach_files=False,
                    add_reactions=False
                ),

            bot_member:
                discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    manage_channels=True,
                    manage_messages=True,
                    read_message_history=True
                )

        }

        chamber = await guild.create_text_channel(

            name=channel_name,

            category=category,

            overwrites=overwrites,

            topic=(
                f"Soul Chamber of {member.display_name}"
            )

        )

        return chamber
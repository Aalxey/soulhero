import discord

from bot.services.channel_service import ChannelService


class SoulChamberService:
    """
    Responsible ONLY for managing a player's Soul Chamber.

    Responsibilities:
    - Find an existing Soul Chamber.
    - Create one if it does not exist.
    - Return the player's Soul Chamber.

    This service NEVER:
    - Sends embeds
    - Sends messages
    - Updates SQL
    - Deletes channels
    - Handles progression
    """

    @staticmethod
    async def get_or_create(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ) -> discord.TextChannel:

        category = ChannelService.get_category(
            guild
        )

        channel_name = (
            f"soul-chamber-{str(member.id)[-4:]}"
        )

        existing_channel = discord.utils.get(

            category.text_channels,

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

                    add_reactions=False,

                    use_application_commands=True

                ),

            bot_member:

                discord.PermissionOverwrite(

                    view_channel=True,

                    send_messages=True,

                    manage_channels=True,

                    manage_messages=True,

                    manage_permissions=True,

                    read_message_history=True,

                    embed_links=True,

                    attach_files=True

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

        await chamber.edit(

            sync_permissions=False

        )

        return chamber
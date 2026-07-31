import discord

from config import SOUL_CORE_CATEGORY_ID


class ChannelService:
    """
    Responsible ONLY for temporary channels.

    Examples:
    - Forgotten Ruins
    - Battle Arena
    - Dungeon
    - Raid
    - Event

    Every channel created here is temporary and
    may later be deleted.
    """

    @staticmethod
    def get_category(
        guild: discord.Guild
    ) -> discord.CategoryChannel:

        category = guild.get_channel(
            SOUL_CORE_CATEGORY_ID
        )

        if category is None:

            raise ValueError(
                "Soul Core category was not found."
            )

        return category


    @staticmethod
    async def get_or_create_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ) -> discord.TextChannel:

        category = ChannelService.get_category(
            guild
        )

        channel_name = (
            f"forgotten-ruins-{str(member.id)[-4:]}"
        )

        existing_channel = discord.utils.get(

            category.text_channels,

            name=channel_name

        )

        if existing_channel is not None:

            await existing_channel.set_permissions(

                guild.default_role,

                view_channel=False

            )

            await existing_channel.set_permissions(

                member,

                view_channel=True,
                read_message_history=True,

                send_messages=False,

                embed_links=False,
                attach_files=False,
                add_reactions=False,

                create_public_threads=False,
                create_private_threads=False,
                send_messages_in_threads=False,

                use_application_commands=True

            )

            await existing_channel.set_permissions(

                bot_member,

                view_channel=True,
                send_messages=True,

                manage_channels=True,
                manage_messages=True,
                manage_permissions=True,

                read_message_history=True,

                embed_links=True,
                attach_files=True

            )

            return existing_channel

        overwrites = {

            guild.default_role:

                discord.PermissionOverwrite(

                    view_channel=False

                ),

            member:

                discord.PermissionOverwrite(

                    view_channel=True,

                    read_message_history=True,

                    send_messages=False,

                    embed_links=False,

                    attach_files=False,

                    add_reactions=False,

                    create_public_threads=False,

                    create_private_threads=False,

                    send_messages_in_threads=False,

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

        channel = await guild.create_text_channel(

            name=channel_name,

            category=category,

            overwrites=overwrites

        )

        await channel.edit(

            sync_permissions=False

        )

        return channel


    @staticmethod
    async def collapse_ruins_channel(
        channel: discord.TextChannel
    ):

        if channel is None:

            return

        await channel.delete(

            reason="Forgotten Ruins collapsed after oath completion."

        )
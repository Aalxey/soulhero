import discord

from config import SOUL_CORE_CATEGORY_ID


class ChannelService:

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
    def get_channel_name(
        member: discord.Member
    ) -> str:

        return (
            f"forgotten-ruins-{str(member.id)[-4:]}"
        )

    @staticmethod
    async def get_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member
    ) -> discord.TextChannel | None:

        category = ChannelService.get_category(
            guild
        )

        channel_name = (
            ChannelService.get_channel_name(
                member
            )
        )

        return discord.utils.get(
            category.channels,
            name=channel_name
        )

    @staticmethod
    async def create_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ) -> discord.TextChannel:

        category = ChannelService.get_category(
            guild
        )

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
                    manage_messages=True
                )
        }

        return await guild.create_text_channel(

            name=ChannelService.get_channel_name(
                member
            ),

            category=category,

            overwrites=overwrites

        )

    @staticmethod
    async def get_or_create_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ) -> discord.TextChannel:

        channel = await ChannelService.get_awakening_chamber(
            guild,
            member
        )

        if channel is not None:

            return channel

        return await ChannelService.create_awakening_chamber(
            guild,
            member,
            bot_member
        )

    @staticmethod
    async def delete_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member
    ):

        channel = await ChannelService.get_awakening_chamber(
            guild,
            member
        )

        if channel is None:

            return

        await channel.delete(
            reason="The Forgotten Ruins have crumbled."
        )
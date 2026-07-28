import discord

from config import SOUL_CORE_CATEGORY_ID


class ChannelService:


    @staticmethod
    async def get_or_create_awakening_chamber(
        guild: discord.Guild,
        member: discord.Member,
        bot_member: discord.Member
    ):


        category = guild.get_channel(
            SOUL_CORE_CATEGORY_ID
        )


        if category is None:

            raise ValueError(
                "Soul Core category was not found."
            )


        channel_name = (
            f"forgotten-ruins-{str(member.id)[-4:]}"
        )


        existing_channel = discord.utils.get(
            category.channels,
            name=channel_name
        )


        if existing_channel:

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
                    manage_messages=True
                )

        }



        return await guild.create_text_channel(

            name=channel_name,

            category=category,

            overwrites=overwrites

        )



    @staticmethod
    async def collapse_ruins_channel(
        channel: discord.TextChannel
    ):

        if channel is None:

            return


        await channel.delete(

            reason="Forgotten Ruins collapsed after oath completion."

        )
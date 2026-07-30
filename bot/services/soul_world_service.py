import discord

from config import SOUL_CORE_CATEGORY_ID


class SoulWorldService:
    """
    Handles creation of a player's permanent Soul World area.

    This service only manages Discord channels.
    It does not handle:
        - player state
        - story
        - progression
    """



    @staticmethod
    async def get_or_create_soul_chamber(
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

            f"soul-world-{str(member.id)[-4:]}"

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

                    embed_links=True

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
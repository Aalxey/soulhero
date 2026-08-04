import discord

from config import SOUL_CORE_CATEGORY_ID


class BattleChannelService:
    """
    Responsible ONLY for battle channels.

    Responsibilities:
    - Create battle channels
    - Return battle channels
    - Delete battle channels

    This service NEVER:
    - Starts battles
    - Sends embeds
    - Updates SQL
    - Calculates damage
    """

    @staticmethod
    def get_category(
        guild: discord.Guild
    ):

        category = guild.get_channel(

            SOUL_CORE_CATEGORY_ID

        )

        if category is None:

            raise ValueError(

                "Soul Core category was not found."

            )

        return category


    @staticmethod
    async def create(

        
        guild: discord.Guild,

        battle,

        player_one: discord.Member,

        player_two: discord.Member,

        bot_member: discord.Member


    ):

        category = BattleChannelService.get_category(

            guild

        )

        channel_name = (

            f"battle-{battle.id[:4].lower()}"

        )


        overwrites = {

            # Everyone can WATCH
            guild.default_role:

                discord.PermissionOverwrite(

                    view_channel=True,

                    read_message_history=True,

                    send_messages=False,

                    add_reactions=False,

                    attach_files=False,

                    create_public_threads=False,

                    create_private_threads=False,

                    send_messages_in_threads=False,

                    use_application_commands=False

                ),

            # Player One
            player_one:

                discord.PermissionOverwrite(

                    view_channel=True,

                    send_messages=True,

                    read_message_history=True,

                    embed_links=True,

                    attach_files=False,

                    use_application_commands=True

                ),

            # Player Two
            player_two:

                discord.PermissionOverwrite(

                    view_channel=True,

                    send_messages=True,

                    read_message_history=True,

                    embed_links=True,

                    attach_files=False,

                    use_application_commands=True

                ),

            # Bot
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
    async def delete(

        channel: discord.TextChannel

    ):

        if channel is None:

            return

        await channel.delete(

            reason="Battle finished."

        )
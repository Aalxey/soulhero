import secrets

import discord


class ChallengeChannelService:

    CATEGORY_NAME = "🏛 Hall of Trials"

    @staticmethod
    async def get_or_create_category(
        guild: discord.Guild
    ):

        for category in guild.categories:

            if category.name == ChallengeChannelService.CATEGORY_NAME:
                return category

        return await guild.create_category(

            ChallengeChannelService.CATEGORY_NAME

        )

    @staticmethod
    async def create(

        guild: discord.Guild,

        challenger: discord.Member,

        challenged: discord.Member,

        bot_member: discord.Member

    ):

        category = await ChallengeChannelService.get_or_create_category(

            guild

        )

        challenge_id = secrets.token_hex(2)

        channel_name = f"challenge-{challenge_id}"

        overwrites = {

            guild.default_role: discord.PermissionOverwrite(

                view_channel=False

            ),

            challenger: discord.PermissionOverwrite(

                view_channel=True,
                send_messages=True,
                read_message_history=True

            ),

            challenged: discord.PermissionOverwrite(

                view_channel=True,
                send_messages=True,
                read_message_history=True

            ),

            bot_member: discord.PermissionOverwrite(

                view_channel=True,
                send_messages=True,
                manage_channels=True,
                manage_messages=True,
                read_message_history=True

            )

        }

        channel = await guild.create_text_channel(

            name=channel_name,

            category=category,

            overwrites=overwrites,

            topic=f"Duel Challenge | {challenger.id} vs {challenged.id}"

        )

        return channel

    @staticmethod
    async def delete(

        channel: discord.TextChannel

    ):

        try:

            await channel.delete(

                reason="Challenge Finished"

            )

        except Exception as e:

            print(

                "ChallengeChannelService.delete():",

                repr(e)

            )
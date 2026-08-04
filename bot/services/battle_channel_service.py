import discord
import random


class BattleChannelService:
    """
    Creates battle channels.

    Responsible ONLY for:
    - creating battle room
    - setting permissions

    Does NOT:
    - manage combat
    - handle turns
    - calculate damage
    """


    @staticmethod
    async def create(
        guild,
        battle,
        player_one,
        player_two,
        bot_member
    ):


        print("\n========== CREATE BATTLE CHANNEL ==========")


        name = f"battle-{random.randint(1000,9999)}"


        print(
            "Creating:",
            name
        )


        overwrites = {

            guild.default_role:
            discord.PermissionOverwrite(
                view_channel=False
            ),


            player_one:
            discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            ),


            player_two:
            discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            ),


            guild.me:
            discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                manage_channels=True,
                manage_messages=True
            )

        }



        channel = await guild.create_text_channel(

            name=name,

            overwrites=overwrites

        )


        print(
            "Battle channel created:",
            channel.name
        )


        print(
            "==========================================\n"
        )


        return channel
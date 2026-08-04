import discord


class BattleCleanupService:
    """
    Cleans temporary battle resources.

    Responsible for:
        - deleting battle channel
        - future cleanup
    """


    @staticmethod
    async def delete_channel(
        battle
    ):

        print("\n")
        print("=" * 50)
        print("🗑 BATTLE CLEANUP START")
        print("=" * 50)


        if not battle.channel_id:

            print(
                "❌ No battle channel ID"
            )

            return



        guild = battle.guild


        if guild is None:

            print(
                "❌ No guild reference"
            )

            return



        channel = guild.get_channel(

            battle.channel_id

        )


        if channel is None:

            print(
                "❌ Battle channel not found"
            )

            return



        print(
            "Deleting:",
            channel.name
        )


        await channel.delete(

            reason="Battle finished"

        )


        print(
            "✅ Battle channel deleted"
        )


        print("=" * 50)
        print()
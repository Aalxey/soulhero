import discord


class BattleRefreshService:


    @staticmethod
    async def refresh(
        interaction: discord.Interaction,
        battle,
        result=None
    ):

        print("\n========== BATTLE REFRESH ==========")


        from bot.scenes.battle_scene import BattleScene
        from bot.views.attack_view import AttackView


        guild = interaction.guild


        if guild is None:

            print("❌ No guild")
            return



        channel = guild.get_channel(
            battle.channel_id
        )


        if channel is None:

            print("❌ Channel missing")
            return



        print(
            "Fetching battle message:",
            battle.message_id
        )



        try:

            message = await channel.fetch_message(

                battle.message_id

            )


        except Exception as e:

            print(
                "❌ Message fetch failed:",
                e
            )

            return



        print(
            "Battle message found:",
            message.id
        )



        scene = BattleScene(

            battle=battle,

            result=result

        )



        print(
            "Editing battle message"
        )



        await message.edit(

            embed=scene.build_embed(),

            view=scene.build_view()

        )



        print(
            "Battle message refreshed"
        )



        # ---------------------------------
        # Send next player's attack menu
        # ---------------------------------


        current_player = battle.current_player()



        if current_player is None:

            print(
                "❌ No current player"
            )

            return



        print(
            "Sending attack menu to:",
            current_player.discord_id
        )



        member = await guild.fetch_member(

            int(current_player.discord_id)

        )



        # await member.send(

        #     "⚔ Choose your skill.",

        #     view=AttackView(

        #         battle,

        #         current_player.discord_id

        #     )

        # )


        print(
            "Attack menu sent"
        )


        print(
            "====================================\n"
        )
import discord

from bot.views.attack_view import AttackView


class BattleScene:
    """
    Responsible for rendering battle UI.

    Does NOT:
        - calculate damage
        - modify HP
        - control turns
        - handle Discord interactions
    """


    def __init__(
        self,
        battle,
        result=None
    ):

        self.battle = battle
        self.result = result

        self.scene_name = "BATTLE"


        print("\n")
        print("=" * 50)
        print("⚔ BATTLE SCENE CREATED")
        print("=" * 50)

        print(
            "Battle ID:",
            id(self.battle)
        )

        print(
            "Battle finished:",
            getattr(
                self.battle,
                "finished",
                False
            )
        )


        if self.result:

            print(
                "Result:",
                self.result.__dict__
            )

        else:

            print(
                "Result: None"
            )


        print("=" * 50)
        print("\n")



    # =================================================
    # EMBED
    # =================================================

    def build_embed(self):


        print(
            "⚔ BUILDING BATTLE EMBED"
        )


        embed = discord.Embed(

            title="⚔ Battle",

            color=discord.Color.red()

        )



        player_one = self.battle.player_one

        player_two = self.battle.player_two



        state_one = self.battle.state_of(

            player_one.discord_id

        )


        state_two = self.battle.state_of(

            player_two.discord_id

        )



        embed.add_field(

            name=f"⚔ {player_one.username}",

            value=(

                f"❤️ HP: {state_one.hp}\n"

                f"⚔ ATK: {state_one.attack}\n"

                f"🛡 DEF: {state_one.defense}"

            ),

            inline=True

        )



        embed.add_field(

            name=f"⚔ {player_two.username}",

            value=(

                f"❤️ HP: {state_two.hp}\n"

                f"⚔ ATK: {state_two.attack}\n"

                f"🛡 DEF: {state_two.defense}"

            ),

            inline=True

        )



        # =================================================
        # RESULT
        # =================================================


        if self.result:


            print(
                "Processing battle result"
            )



            if self.result.finished:


                print(
                    "🏆 Adding winner"
                )


                winner = self.result.winner



                winner_name = (

                    winner.username

                    if winner

                    else

                    "Unknown"

                )



                embed.add_field(

                    name="🏆 Victory",

                    value=(

                        f"{winner_name}"

                        "\n\n"

                        "The battle has ended."

                    ),

                    inline=False

                )


            elif self.result.damage:


                embed.add_field(

                    name="🩸 Damage",

                    value=(

                        f"{self.result.damage}"

                    ),

                    inline=False

                )




        # =================================================
        # CURRENT TURN
        # =================================================


        if (

            not self.result

            or

            not self.result.finished

        ):


            current = self.battle.current_player()



            if current:


                embed.add_field(

                    name="🎯 Current Turn",

                    value=current.username,

                    inline=False

                )


                print(

                    "Current turn:",

                    current.username

                )



        else:


            print(

                "Battle finished."

                " No turn display."

            )



        print(
            "✅ EMBED READY"
        )


        return embed





    # =================================================
    # VIEW
    # =================================================

    def build_view(self):


        print("\n")
        print("=" * 50)
        print("⚔ BUILDING BATTLE VIEW")
        print("=" * 50)



        # -----------------------------------------
        # Result says finished
        # -----------------------------------------


        if self.result:


            print(

                "Checking result finished:",

                self.result.finished

            )



            if self.result.finished:


                print(

                    "🏆 RESULT FINISHED"

                )


                print(

                    "Returning None view"

                )


                print("=" * 50)
                print("\n")


                return None





        # -----------------------------------------
        # Battle object finished
        # -----------------------------------------


        if getattr(

            self.battle,

            "finished",

            False

        ):


            print(

                "🏆 BATTLE OBJECT FINISHED"

            )


            print(

                "Returning None view"

            )


            print("=" * 50)
            print("\n")


            return None




        # -----------------------------------------
        # Check winner directly
        # -----------------------------------------


        if hasattr(

            self.battle,

            "winner"

        ) and self.battle.winner:


            print(

                "🏆 Winner exists"

            )


            print(

                "Returning None view"

            )


            return None





        # -----------------------------------------
        # Create attack menu
        # -----------------------------------------


        player = self.battle.current_player()



        if player is None:


            print(

                "❌ No current player"

            )


            return None




        print(

            "Creating AttackView"

        )


        print(

            "Player:",

            player.username

        )


        print(

            "Player ID:",

            player.discord_id

        )



        view = AttackView(

            self.battle,

            str(player.discord_id)

        )



        print(

            "✅ AttackView created"

        )


        print("=" * 50)
        print("\n")



        return view
import asyncio
import traceback

import discord

from bot.services.challenge_channel_service import ChallengeChannelService
from bot.battle.battle_manager import BattleManager
from bot.services.battle_channel_service import BattleChannelService
from bot.scenes.battle_scene import BattleScene
from bot.engine.scene_manager import SceneManager



class ChallengeView(discord.ui.View):

    def __init__(
        self,
        challenger,
        challenged,
        hero
    ):

        super().__init__(
            timeout=120
        )

        self.challenger = challenger
        self.challenged = challenged
        self.hero = hero

        self.finished = False

        print(
            "⚔ ChallengeView created"
        )



    # -------------------------------------------------
    # ONLY CHALLENGED PLAYER CAN ANSWER
    # -------------------------------------------------

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        print(
            "Challenge interaction:",
            interaction.user
        )


        if str(interaction.user.id) != self.challenged.discord_id:

            print(
                "❌ Wrong player pressed button"
            )


            await interaction.response.send_message(

                "🌑 This challenge does not belong to your soul.",

                ephemeral=True

            )


            return False


        print(
            "✅ Challenge owner verified"
        )


        return True



    # -------------------------------------------------
    # ACCEPT DUEL
    # -------------------------------------------------

    @discord.ui.button(
        label="⚔ Accept the Duel",
        style=discord.ButtonStyle.success
    )
    async def accept(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        print("\n")
        print("=" * 60)
        print("⚔ DUEL ACCEPTED")
        print("=" * 60)


        try:


            self.finished = True



            print(
                "1. Editing challenge message"
            )


            await interaction.response.edit_message(

                embed=discord.Embed(

                    title="⚔ Challenge Accepted",

                    description=(

                        "The Hall of Trials acknowledges both souls.\n\n"

                        "The Ancient Arena begins to awaken..."

                    ),

                    color=discord.Color.gold()

                ),

                view=None

            )


            print(
                "2. Creating battle object"
            )


            battle = BattleManager.create(

                self.challenger,

                self.challenged

            )

            battle.guild = interaction.guild


            print(
                "Battle created:",
                battle
            )


            print(
                "3. Fetching members"
            )


            player_one_member = await interaction.guild.fetch_member(

                int(self.challenger.discord_id)

            )


            player_two_member = await interaction.guild.fetch_member(

                int(self.challenged.discord_id)

            )


            bot_member = await interaction.guild.fetch_member(

                interaction.client.user.id

            )


            print(
                "PLAYER ONE:",
                player_one_member
            )

            print(
                "PLAYER TWO:",
                player_two_member
            )

            print(
                "BOT:",
                bot_member
            )



            print(
                "4. Creating battle channel"
            )


            battle_channel = await BattleChannelService.create(

                guild=interaction.guild,

                battle=battle,

                player_one=player_one_member,

                player_two=player_two_member,

                bot_member=bot_member

            )


            battle.channel = battle_channel
            battle.channel_id = battle_channel.id


            print(
                "Battle channel:",
                battle_channel.name
            )


            print(
                "Battle channel ID:",
                battle.channel_id
            )



            print(
                "5. Creating battle scene"
            )


            scene = BattleScene(

                battle

            )



            print(
                "6. Sending battle scene"
            )


            message = await SceneManager.send(

                battle_channel,

                scene

            )


            print(
                "Battle message received:",
                message
            )


            print(
                "Battle message ID:",
                message.id
            )


            # ---------------------------------
            # IMPORTANT FIX
            # ---------------------------------

            battle.message_id = message.id


            print(
                "Saved battle.message_id:",
                battle.message_id
            )



            print(
                "7. Battle ready"
            )



            await asyncio.sleep(2)



            print(
                "8. Deleting challenge room"
            )


            await ChallengeChannelService.delete(

                interaction.channel

            )


            print(
                "9. Challenge room deleted"
            )



            print("=" * 60)
            print("⚔ DUEL STARTED SUCCESSFULLY")
            print("=" * 60)
            print("\n")



        except Exception:


            print("\n")
            print("=" * 60)
            print("❌ DUEL ACCEPT ERROR")
            print("=" * 60)


            traceback.print_exc()


            print("=" * 60)
            print("\n")



            try:


                if not interaction.response.is_done():


                    await interaction.response.send_message(

                        "⚔ The duel could not begin.",

                        ephemeral=True

                    )

                else:


                    await interaction.followup.send(

                        "⚔ The duel could not begin.",

                        ephemeral=True

                    )


            except Exception:

                pass




    # -------------------------------------------------
    # IGNORE CHALLENGE
    # -------------------------------------------------

    @discord.ui.button(

        label="🌑 Ignore the Scroll",

        style=discord.ButtonStyle.secondary

    )
    async def ignore(

        self,

        interaction: discord.Interaction,

        button: discord.ui.Button

    ):


        self.finished = True


        await interaction.response.edit_message(

            embed=discord.Embed(

                title="📜 Challenge Declined",

                description=(

                    "The scroll turns to ash.\n\n"

                    "The raven disappears into the darkness."

                ),

                color=discord.Color.dark_grey()

            ),

            view=None

        )


        await asyncio.sleep(3)


        await ChallengeChannelService.delete(

            interaction.channel

        )




    # -------------------------------------------------
    # TIMEOUT
    # -------------------------------------------------

    async def on_timeout(self):


        if self.finished:

            return



        self.finished = True



        if self.message is None:

            return



        embed = discord.Embed(

            title="📜 Challenge Expired",

            description=(

                "The crimson seal fades.\n\n"

                "The raven takes the unanswered scroll "

                "and disappears into the night.\n\n"

                "No duel shall take place."

            ),

            color=discord.Color.red()

        )


        try:


            await self.message.edit(

                embed=embed,

                view=None

            )


            await asyncio.sleep(5)


            await ChallengeChannelService.delete(

                self.message.channel

            )


        except Exception:


            pass
import discord

from bot.engine.scene_manager import SceneManager
from bot.engine.message_manager import MessageManager


class SceneRecoveryService:
    """
    Restores deleted or missing scene messages.

    Responsible for:
        - checking existing scene message
        - validating Discord message
        - validating the saved message belongs to the
          requested scene, not a stale earlier scene
        - recreating scene if needed

    Does NOT:
        - change journey state
        - decide progression
    """


    @staticmethod
    async def restore(
        player,
        channel: discord.TextChannel,
        scene_class,
        hero=None
    ):

        print("\n" + "="*60)
        print("🔍 SCENE RECOVERY START")
        print("="*60)
        print(f"Player: {player.username} ({player.discord_id})")
        print(f"Requested Scene: {scene_class.__name__}")
        print(f"Channel: {channel.name} ({channel.id})")
        print(f"Hero: {hero}")


        saved = MessageManager.get(
            player.discord_id
        )


        print(f"\n📋 Checking MessageManager...")
        if saved:
            print(f"✓ Found saved message:")
            print(f"  - message_id: {saved.get('message_id')}")
            print(f"  - channel_id: {saved.get('channel_id')}")
            print(f"  - scene_name: {saved.get('scene_name')}")
        else:
            print(f"✗ No saved message in MessageManager")


        # --------------------------------
        # Check existing message
        # --------------------------------

        if saved:

            requested_scene_name = scene_class.__name__.replace(

                "Scene",

                ""

            ).upper()

            saved_scene_name = saved.get("scene_name")

            print(f"\n🔎 Validating scene type...")
            print(f"  Saved scene: {saved_scene_name}")
            print(f"  Requested scene: {requested_scene_name}")

            if saved_scene_name != requested_scene_name:

                print(f"⚠️  STALE SCENE DETECTED!")
                print(f"   This is an old {saved_scene_name} scene")
                print(f"   We need a {requested_scene_name} scene")
                print(f"   Removing stale entry...")

                MessageManager.remove(
                    player.discord_id
                )

                print(f"✓ Stale scene removed from MessageManager")

                saved = None


        if saved:

            print(f"\n📤 Attempting to fetch existing message...")

            try:

                old_channel = channel.guild.get_channel(

                    int(saved["channel_id"])

                )

                if not old_channel:
                    print(f"✗ Channel not found (ID: {saved['channel_id']})")
                    raise Exception("Channel not accessible")

                print(f"✓ Channel found: {old_channel.name}")

                old_message = await old_channel.fetch_message(

                    int(saved["message_id"])

                )

                print(f"✓ Message found (ID: {old_message.id})")
                print(f"📝 Message content preview: {old_message.content[:50]}...")

                print(f"\n🗑️  Deleting old message...")
                await old_message.delete()

                print(f"✓ Old message deleted successfully")


            except discord.NotFound:

                print(f"✗ Message not found (already deleted)")

                MessageManager.remove(
                    player.discord_id
                )

                print(f"✓ Removed stale entry from MessageManager")


            except discord.Forbidden:

                print(f"✗ No permission to access/delete message")

                MessageManager.remove(
                    player.discord_id
                )

                print(f"✓ Removed entry from MessageManager")


            except Exception as e:

                print(f"✗ Error fetching/deleting: {repr(e)}")

                MessageManager.remove(
                    player.discord_id
                )

                print(f"✓ Removed entry from MessageManager")


            print(f"✓ Removed from MessageManager (cleanup)")


        # --------------------------------
        # Create new scene
        # --------------------------------

        print(f"\n✨ Creating new scene...")
        print(f"   Scene class: {scene_class.__name__}")

        try:

            if hero is None:

                print(f"   Creating without hero...")

                scene = scene_class(
                    player
                )

            else:

                print(f"   Creating with hero: {hero}")

                scene = scene_class(
                    player,
                    hero
                )

            print(f"✓ Scene object created")

        except Exception as e:

            print(f"✗ Failed to create scene object: {repr(e)}")
            raise


        print(f"\n📨 Sending scene to Discord...")

        try:

            message = await SceneManager.send(
                channel,
                scene
            )

            print(f"✓ Scene sent successfully!")
            print(f"   Message ID: {message.id}")
            print(f"   Channel: {message.channel.name}")
            print(f"   Content length: {len(message.content)} chars")

        except Exception as e:

            print(f"✗ Failed to send scene: {repr(e)}")
            raise


        print(f"\n" + "="*60)
        print(f"✅ SCENE RECOVERY COMPLETE")
        print(f"="*60 + "\n")

        return message
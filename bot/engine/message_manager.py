class MessageManager:
    """
    Keeps track of the active Discord message
    for each player's current scene.

    For now this is stored in memory.

    Later this will move into SQL without
    changing the rest of the engine.
    """

    _messages = {}

    @classmethod
    def save(

        cls,

        discord_id,

        channel_id,

        message_id,

        scene_name

    ):

        cls._messages[str(discord_id)] = {

            "channel_id": channel_id,

            "message_id": message_id,

            "scene": scene_name

        }

    @classmethod
    def get(

        cls,

        discord_id

    ):

        return cls._messages.get(

            str(discord_id)

        )

    @classmethod
    def remove(

        cls,

        discord_id

    ):

        cls._messages.pop(

            str(discord_id),

            None

        )
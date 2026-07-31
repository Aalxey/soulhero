from bot.database.connection import SessionLocal
from bot.database.models import Player
from bot.utils.constants import JourneyState


session = SessionLocal()

try:

    player = (
        session.query(Player)
        .filter(
            Player.discord_id == "762322750978916362"
        )
        .first()
    )


    if player:

        player.journey_state = JourneyState.OATHBOUND

        session.commit()

        print(
            "Player updated to OATHBOUND"
        )

    else:

        print(
            "Player not found"
        )


finally:

    session.close()
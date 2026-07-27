from bot.database.connection import SessionLocal
from bot.database.models import Player


class PlayerRepository:

    @staticmethod
    def get_by_discord_id(discord_id: str):
        session = SessionLocal()

        try:
            return (
                session.query(Player)
                .filter(Player.discord_id == discord_id)
                .first()
            )
        finally:
            session.close()

    @staticmethod
    def create_player(discord_id: str, username: str):
        session = SessionLocal()

        try:
            player = Player(
                discord_id=discord_id,
                username=username,
                journey_state="WANDERER"
            )

            session.add(player)
            session.commit()
            session.refresh(player)

            return player

        finally:
            session.close()
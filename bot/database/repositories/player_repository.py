from bot.database.connection import SessionLocal
from bot.database.models import Player


class PlayerRepository:

    @staticmethod
    def get_by_discord_id(discord_id: str):
        session = SessionLocal()

        try:
            return (
                session.query(Player)
                .filter(Player.discord_id == str(discord_id))
                .first()
            )

        finally:
            session.close()

    @staticmethod
    def create(
        discord_id: str,
        username: str
    ):
        session = SessionLocal()

        try:

            player = Player(
                discord_id=str(discord_id),
                username=username,
                journey_state="WANDERER"
            )

            session.add(player)

            session.commit()

            session.refresh(player)

            return player

        finally:
            session.close()

    @staticmethod
    def save(player):
        session = SessionLocal()

        try:

            merged_player = session.merge(player)

            session.commit()

            session.refresh(merged_player)

            return merged_player

        finally:
            session.close()

    @staticmethod
    def update(player, **fields):
        session = SessionLocal()

        try:

            db_player = (
                session.query(Player)
                .filter(Player.id == player.id)
                .first()
            )

            if db_player is None:
                return None

            for key, value in fields.items():

                setattr(
                    db_player,
                    key,
                    value
                )

            session.commit()

            session.refresh(db_player)

            return db_player

        finally:
            session.close()

    @staticmethod
    def delete(player):
        session = SessionLocal()

        try:

            db_player = (
                session.query(Player)
                .filter(Player.id == player.id)
                .first()
            )

            if db_player is None:
                return

            session.delete(db_player)

            session.commit()

        finally:
            session.close()
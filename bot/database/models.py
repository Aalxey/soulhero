from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from bot.database.connection import Base


class Player(Base):

    __tablename__ = "players"


    id = Column(
        Integer,
        primary_key=True
    )


    discord_id = Column(
        String,
        unique=True,
        nullable=False
    )


    username = Column(
        String,
        nullable=False
    )


    # The Hero bonded with this player
    # None means no Hero chosen yet

    hero_id = Column(
        Integer,
        nullable=True
    )


    journey_state = Column(
        String,
        default="WANDERER"
    )


    oathbound_date = Column(
        DateTime,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
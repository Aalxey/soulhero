from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

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


    hero_id = Column(
        Integer,
        nullable=True
    )


    journey_state = Column(
        String,
        default="WANDERER",
        nullable=False
    )


    # Player progression
    resonance = Column(
        Integer,
        default=1,
        nullable=False
    )


    # PvP statistics
    wins = Column(
        Integer,
        default=0,
        nullable=False
    )


    losses = Column(
        Integer,
        default=0,
        nullable=False
    )


    oathbound_date = Column(
        DateTime,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
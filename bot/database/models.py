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

    # -----------------------------------------
    # Progression
    # -----------------------------------------

    resonance = Column(
        Integer,
        default=1,
        nullable=False
    )

    # Manual stat points earned every 5 Resonance
    allocated_hp = Column(
        Integer,
        default=0,
        nullable=False
    )

    allocated_attack = Column(
        Integer,
        default=0,
        nullable=False
    )

    allocated_defense = Column(
        Integer,
        default=0,
        nullable=False
    )

    allocated_speed = Column(
        Integer,
        default=0,
        nullable=False
    )

    # Permanent Fortune stat
    luck = Column(
        Integer,
        default=1,
        nullable=False
    )

    # -----------------------------------------
    # PvP
    # -----------------------------------------

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

    # -----------------------------------------
    # Journey
    # -----------------------------------------

    oathbound_date = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
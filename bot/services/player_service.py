from datetime import datetime

from bot.database.connection import SessionLocal
from bot.database.models import Player

from bot.utils.constants import JourneyState


class PlayerService:


    @staticmethod
    def get_player(discord_id):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )

            return player

        finally:

            db.close()



    @staticmethod
    def create_player(
        discord_id,
        username
    ):

        db = SessionLocal()

        try:

            existing_player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if existing_player:

                return existing_player



            player = Player(

                discord_id=str(discord_id),

                username=username,

                journey_state=JourneyState.WANDERER

            )


            db.add(player)

            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def update_journey_state(
        discord_id,
        state
    ):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if not player:

                return None



            player.journey_state = state


            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def assign_hero(
        discord_id,
        hero_id
    ):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if not player:

                return None



            # One soul can only bond with one Hero

            if player.hero_id is not None:

                return player



            player.hero_id = hero_id


            player.journey_state = (
                JourneyState.HERO_CHOSEN
            )


            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def complete_oath(
        discord_id
    ):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if not player:

                return None



            # Oath can only happen after choosing a Hero

            if player.hero_id is None:

                return player



            player.journey_state = (
                JourneyState.OATH_COMPLETE
            )


            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def enter_welcome(
        discord_id
    ):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if not player:

                return None



            # Welcome only after oath

            if player.journey_state != JourneyState.OATH_COMPLETE:

                return player



            player.journey_state = (
                JourneyState.WELCOME
            )


            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def collapse_ruins(
        discord_id
    ):

        db = SessionLocal()

        try:

            player = (
                db.query(Player)
                .filter(
                    Player.discord_id == str(discord_id)
                )
                .first()
            )


            if not player:

                return None



            # Ruins can only collapse after welcome

            if player.journey_state != JourneyState.WELCOME:

                return player



            player.journey_state = (
                JourneyState.OATHBOUND
            )


            player.oathbound_date = (
                datetime.utcnow()
            )


            db.commit()

            db.refresh(player)


            return player


        finally:

            db.close()



    @staticmethod
    def is_oathbound(
        discord_id
    ):

        player = (
            PlayerService.get_player(
                discord_id
            )
        )


        if not player:

            return False



        return (
            player.journey_state
            ==
            JourneyState.OATHBOUND
        )
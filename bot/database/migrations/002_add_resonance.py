from sqlalchemy import text


def up(connection):

    columns = connection.execute(

        text(

            "PRAGMA table_info(players)"

        )

    ).fetchall()


    existing_columns = {

        column[1]

        for column in columns

    }


    if "resonance" not in existing_columns:

        connection.execute(

            text(

                """
                ALTER TABLE players
                ADD COLUMN resonance INTEGER NOT NULL DEFAULT 1
                """

            )

        )


    if "wins" not in existing_columns:

        connection.execute(

            text(

                """
                ALTER TABLE players
                ADD COLUMN wins INTEGER NOT NULL DEFAULT 0
                """

            )

        )


    if "losses" not in existing_columns:

        connection.execute(

            text(

                """
                ALTER TABLE players
                ADD COLUMN losses INTEGER NOT NULL DEFAULT 0
                """

            )

        )


    connection.commit()
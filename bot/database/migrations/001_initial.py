from sqlalchemy import text


def up(connection):

    connection.execute(

        text(

            """
            CREATE TABLE IF NOT EXISTS migrations
            (
                version INTEGER PRIMARY KEY
            )
            """

        )

    )

    connection.commit()
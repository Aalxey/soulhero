from sqlalchemy import text


def up(connection):

    columns = [

        (
            "allocated_hp",
            "INTEGER DEFAULT 0"
        ),

        (
            "allocated_attack",
            "INTEGER DEFAULT 0"
        ),

        (
            "allocated_defense",
            "INTEGER DEFAULT 0"
        ),

        (
            "allocated_speed",
            "INTEGER DEFAULT 0"
        ),

        (
            "luck",
            "INTEGER DEFAULT 0"
        )

    ]


    for column_name, column_type in columns:

        connection.execute(

            text(
                f"""
                ALTER TABLE players
                ADD COLUMN {column_name} {column_type}
                """
            )

        )
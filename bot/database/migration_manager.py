import importlib
import os

from sqlalchemy import text

from bot.database.connection import engine


MIGRATION_PACKAGE = "bot.database.migrations"
MIGRATION_DIRECTORY = "bot/database/migrations"


class MigrationManager:

    @staticmethod
    def _migration_table_exists(connection):

        result = connection.execute(

            text(

                """
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                AND name='migrations'
                """

            )

        ).fetchone()

        return result is not None


    @staticmethod
    def _current_version(connection):

        if not MigrationManager._migration_table_exists(
            connection
        ):

            return 0


        result = connection.execute(

            text(

                """
                SELECT MAX(version)
                FROM migrations
                """

            )

        ).fetchone()


        if result is None:

            return 0


        if result[0] is None:

            return 0


        return result[0]


    @staticmethod
    def _save_version(
        connection,
        version
    ):

        connection.execute(

            text(

                """
                INSERT INTO migrations(version)
                VALUES(:version)
                """

            ),

            {

                "version": version

            }

        )

        connection.commit()


    @staticmethod
    def _available_migrations():

        migrations = []

        for file in os.listdir(
            MIGRATION_DIRECTORY
        ):

            if (
                file.endswith(".py")
                and file[:3].isdigit()
            ):

                migrations.append(file)

        migrations.sort()

        return migrations


    @classmethod
    def run(cls):

        with engine.connect() as connection:

            current = cls._current_version(
                connection
            )

            for file in cls._available_migrations():

                version = int(
                    file[:3]
                )

                if version <= current:

                    continue

                module = importlib.import_module(

                    f"{MIGRATION_PACKAGE}.{file[:-3]}"

                )

                print(
                    f"Running migration {version}..."
                )

                module.up(connection)

                cls._save_version(

                    connection,

                    version

                )

                print(
                    f"Migration {version} complete."
                )
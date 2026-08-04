import asyncio

import discord
from discord.ext import commands

from config import DISCORD_TOKEN

from bot.database.connection import Base, engine
from bot.database import models
from bot.database.migration_manager import MigrationManager


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(

    command_prefix="!",

    intents=intents

)


async def load_extensions():

    await bot.load_extension(
        "bot.commands.start"
    )

    await bot.load_extension(
        "bot.commands.profile"
    )

    await bot.load_extension(
        "bot.commands.battle"
    )

@bot.event
async def on_ready():

    try:

        synced = await bot.tree.sync()

        print(
            f"Synced {len(synced)} command(s)."
        )

        for command in synced:
            print(command.name)

    except Exception as e:

        print(e)

    print(
        f"{bot.user} has awakened!"
    )


async def main():

    print("\n========== Soul World ==========")

    print("Creating database schema...")

    Base.metadata.create_all(bind=engine)

    print("Checking migrations...")

    MigrationManager.run()

    print("Database ready.")

    print("Loading Soul World...")

    async with bot:

        await load_extensions()

        await bot.start(
            DISCORD_TOKEN
        )


asyncio.run(main())
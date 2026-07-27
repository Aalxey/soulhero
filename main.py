import discord
from discord.ext import commands
from config import DISCORD_TOKEN
import asyncio
from bot.database.connection import engine, Base
from bot.database import models

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


async def load_extensions():
    await bot.load_extension("bot.commands.start")


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(e)

    print(f"{bot.user} has awakened!")


async def main():

    Base.metadata.create_all(engine)

    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)


asyncio.run(main())
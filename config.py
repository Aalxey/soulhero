import os
from dotenv import load_dotenv

load_dotenv()
SOUL_CORE_CATEGORY_ID = int(os.getenv("SOUL_CORE_CATEGORY_ID"))

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
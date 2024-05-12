import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

BOT_SECRET = os.getenv("BOT_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent

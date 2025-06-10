import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_AUTH_TOKEN = os.getenv('BOT_AUTH_TOKEN', '')  # TODO: add twitch auth token here before running
    BOT_NAME = os.getenv('BOT_NAME', 'AurielBot')
    CHANNELS = os.getenv('CHANNELS', 'Ninjakaing')

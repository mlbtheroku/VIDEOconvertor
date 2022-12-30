from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 15830858, cast=int)
API_HASH = config("API_HASH", "2c015c994c57b312708fecc8a2a0f1a6")
BOT_TOKEN = config("BOT_TOKEN", "5410658090:AAFiwio1AMM7hS9FZShr1Evmjw59lA2lRMo")
BOT_UN = config("BOT_UN", "AIO_Video_Tools_Bot")
AUTH_USERS = config("AUTH_USERS", 5468192421, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", "AIOBOTLOG")
LOG_ID = config("LOG_ID", "-1001749073420")
FORCESUB = config("FORCESUB", "-1001767363693")
FORCESUB_UN = config("FORCESUB_UN", "subtouse")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", "-1001631866019")
MONGODB_URI = config("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

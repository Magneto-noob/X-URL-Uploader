import os
from pyrogram.types import BotCommand
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help message'),
        BotCommand('caption', 'custom caption'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('ban', 'ban user'),
        BotCommand('unban', 'unban user'),
        BotCommand('broadcast', 'broadcast message')
    ]

    DUMP_ID = "-1001567964220"

    BOT_TOKEN = "2049170894:AAEtQ6CFBPqhR4api99FqmO56xArWcE0H-o"

    APP_ID = "15523035"
    API_HASH = "33a37e968712427c2e7971cb03f341b3"

    # Authorized User IDS
    AUTH_USERS = [int(id) for id in os.environ.get(
        "AUTH_USERS", "").split()] if os.environ.get("AUTH_USERS", None) else None

    OWNER_ID = "910674886"

    # MongoDB
    DATABASE_URL = "mongodb+srv://TGBot:Save@koyeb.vvt99ro.mongodb.net/?retryWrites=true&w=majority&appName=Koyeb"

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # watermark file
    DEF_WATER_MARK_FILE = ""

    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

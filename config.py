import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 25625520))
API_HASH = getenv("API_HASH", "b8d327b196bae9b4c72e93a7395b8f05")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6127476417:AAEmNFj34bFiHLwvozMHbBQrhIIzCVrzgGg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1001573382350))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8163570519))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DilwarHosen/AloneAvex",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+mscRligFCLo0ZDY1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-for-AloneXMusic-12-01")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BQGHA7AAey83BNNgUJ44OV9JJDzZDfyHjRcQR-z81dhDU3CMdAjG2U7l7dIIN4w7Uasre2fMyfQJkP7EbQMujCEdpsQTu-pS7mv2mgwsgB4dp7qnKnhlFiJJXrOXsJgBWpqaukpiD5RgioPYIAS28hHgkLIrafm3j_huaUBnOYKrEYcuQNb--17Bs-Oda7J7ziy73WJ9y1rZ8N1kj3szB21FrNCyYXAbVMV2sr-TZN0xCPIG9Wa0Ljtk_OGJdv5nxabR0NI1kj4J0IRnslFXuownlLVT-7ZZxnyJN_n-XISQ32Xu_iOURA-FAc_6USoLQnnO4I6sISVOrXoEcLSJLGVZ35eoSAAAAAG2UkNcAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/s7iujk.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/s7iujk.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
STATS_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/s7iujk.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/s7iujk.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/s7iujk.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

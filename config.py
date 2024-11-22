from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("27758016"))
API_HASH = getenv("8d34cfffe27ab461eabbf0091b1a27df")

BOT_TOKEN = getenv("7944175084:AAFNDr6fIKd4t__0Nj0yrMtrdXe2vY_FrHs")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 7224419362))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/The_Architect04")

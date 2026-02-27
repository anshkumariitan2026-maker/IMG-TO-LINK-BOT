from os import environ
from dotenv import load_dotenv

load_dotenv()

def str_to_bool(val):
    return str(val).lower() in {"true", "yes", "1", "t", "y"}

API_ID = int(environ.get('API_ID'))
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get("BOT_TOKEN")
PORT = environ.get("PORT", "8080")
START_PIC = environ.get("START_PIC")

ADMINS = list(map(int, environ.get("ADMINS").split()))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL"))
DB_URL = environ.get('DATABASE_URI')

AUTH_CHANNEL = list(map(int, environ.get("AUTH_CHANNEL").split()))
AUTH_REQ_CHANNEL = list(map(int, environ.get("AUTH_REQ_CHANNELS").split()))
FSUB = str_to_bool(environ.get("FSUB", "True"))
AUTH_PICS = environ.get("AUTH_PICS")
CHANNEL = environ.get("CHANNEL")
SUPPORT = environ.get("SUPPORT")
APP_URL = environ.get("APP_URL")

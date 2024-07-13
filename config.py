import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24379138"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ddaa43224616428493204bbd8dbf93b1")

#Database 
DB_URI = os.environ.get("DB_URI", "")

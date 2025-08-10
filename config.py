import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7503177601:AAH-5OaP7IBCGh09HOkVWf32zWW4712nTEY")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22451708"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "288f749fcef814c1ec90b66936158c68")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002611123609"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6180759790"))

# Port
PORT = os.environ.get("PORT", "8040")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ganeshgite708:vhovfzpFGRTKVI2O@cluster0.sctr2i3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Shun")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002318367900"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002662363783"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/8ff3ad679a8d46214e418-6080b447bc548aeaab.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/554a276f9bd0622e7ca71-1cb05f4bf2d4adfc88.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Anime_Mortals\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻Developed by <a href=https://t.me/GPGMS0>GPG</a></b>"
ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/GPGMS0>GPG</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_Mortals>Anime Mortals</a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_Mortals>Ongoing Mortals</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/GPGMS0>GPG</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Anime_Mortals</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6180759790").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_Mortals"

ADMINS.append(OWNER_ID)
ADMINS.append(6180759790)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....

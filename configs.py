# (c) @MRK_YT

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

ð¤ **My Name:** [Files Storage Bot](https://t.me/{BOT_USERNAME})

ð **Language:** [Python3](https://www.python.org)

ð **Library:** [Pyrogram](https://docs.pyrogram.org)

ð¡ **Hosted on:** [Heroku](https://heroku.com)

ð§ð»â **Developer:** @SiPmks

ðº **Support:** [YouTube Channel](https://youtube.com/c/LoLyz)

ð£ï¸ **Any Doubt:** @LgViral

ð¢ **Updates Channel:** [Discovery Projects](https://t.me/LendirTelegram)
"""
	ABOUT_DEV_TEXT = f"""
ð§ð»â **Developer:** @SiPmks

ð£ï¸ **Any Doubt:** @LgViral

ðº **Support :** [YouTube Channel](https://youtube.com/c/LoLyz)

ð¢ **Updates Channel:** [Discovery Projects](https://t.me/LendirTelegram)

Donate Now (coming soon)
"""
	HOME_TEXT = """
**ðHi**, [{}](tg://user?id={})\n\n**This is Permanent** **File Storage Lendir Telegram**.

**Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button**.
"""


class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "8162228920"
    sudo_users = (0,)
    GROUP_ID = -1003982219835
    TOKEN = "8721566005:AAHvdIHLgElJRBgdr8WaVaG8UXnndUevZAE"
    mongo_url = ""
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "NARUTO_MUC_SUPPORT_GC"
    UPDATE_CHAT = "logs_45626"
    BOT_USERNAME = "slayer_wh_catcher_bot"
    CHARA_CHANNEL_ID = -1003752709860
    api_id = 37535960
    api_hash = "e89c6a21da912026e645f4132bd4eba7"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

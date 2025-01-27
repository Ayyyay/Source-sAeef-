from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("25992136"))
API_HASH = getenv("18915ee110be6f73362ca7b070844010")

BOT_TOKEN = getenv("7836399013:AAH7JtKAilOsrLp0Xf7mHPP2vVw4thaQvcw", None)
DURATION_LIMIT = int(getenv("xMcki", "90"))

OWNER_ID = int(getenv("nnrsr"))

PING_IMG = getenv("PING_IMG", "https://https://a.top4top.io/p_2929boy350.jpg")
START_IMG = getenv("START_IMG", "https://https://a.top4top.io/p_2929boy350.jpg")

SESSION = getenv("AgCIVfMAiBWh4qAMRfDESY0e_bWuMxxfff2A-ZkDytxxQXZ_X6lnScRb_VZK4u4SKZO4XyaY127a4DjwWdHXIDNy8GQ6iH1aK_ukejgHRY6I5acDewZIxuadz7nX4skFDrpL3DvPXo-yyuFicDNRwdZ1_UN_bdwEVJinyEKdsEDkNLwImLxVuKy_7Fo3-CVZ5f8GgZBLwIMN8Kwn-4dpQmFiXsuyhM7TectewTDiLmF-UWH-W22hQiPF0jpfYr4SRrVVSQCWthkxNs57gsq96VH3St9JZquLPErZy3OI46cT4w8A2DsFyKasmwzWS0S8bP8n78bInW9xzYckMeFIxL-uLDqsxwAAAAHJfzjcAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vvlrl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vvlrl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6326221634").split()))


FAILED = "https://a.top4top.io/p_2929boy350.jpg"

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12850056")

API_HASH = os.environ.get("API_HASH", "15564ec4a1a2cbef87c99a9aa9e40b34")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6656522620:AAGLN6e3rYujnB_T7IhWJt7emZj5biv63mE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "krbackup") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "kdbhaifreefire")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://kdbhaifreefire:7872278427kd@kdbhaifreefire.sqwqyrn.mongodb.net/?retryWrites=true&w=majority&appName=Kdbhaifreefire")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

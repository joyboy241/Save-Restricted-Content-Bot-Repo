# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "10758818"))
API_HASH = getenv("API_HASH", "04fbbf6e526799e099494e33c891aa95")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "728470953"))
MONGODB_CONNECTION_STRING = getenv("MONGODB_CONNECTION_STRING", "mongodb+srv://joyboi242:deepak!123@atlascluster.58jejo7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
LOG_GROUP = int(getenv("LOG_GROUP", "-1001692940921"))
FORCESUB = getenv("FORCESUB", "-1001566404913")

import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @MXnitro")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7126559557:AAEPA-Si5ZEEhx3E3cHFNKH4DdRcWbQZOtQ') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 26305721)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', 'f7fabb6bb9951b499e66f7c44331011d')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 6408829655))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1002103794036)    # Must Fill This ,Add Bot As Admin In Log Channel
BOT_NAME = os.environ.get('BOT_NAME', 'OOxVideoEncodedBot')
#<-----------Variables For 4GB Support (Optional)-------------->
SESSION_STRING = os.environ.get("SESSION_STRING",'None')  #Replace None With String Session   Your String Session Account Must Be Present In Log Channel
ubot = None  # Don't Touch This
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @Devilharsha || Telegram @Mxnitro ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
#<---------------4GB Connecting-------------->
def create_ubot():
    global SESSION_STRING
    global ubot
    if SESSION_STRING != "None":
        try:
            ubot = Client("AutoEncoder", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH, plugins=plugins)
            LOGS.info("❤️ 4GB String Session Connected")
            return ubot
        except:
            LOGS.info('😞 Error While Connecting To String Session')    
            sys.exit()   
            return None

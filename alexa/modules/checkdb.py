import asyncio
import datetime
import time
import pytz
from alexa import tbot, SQLDATEALERT
from telethon import events

@tbot.on(events.NewMessage(pattern=""))
async def check_db():
    LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    OT = LT.strftime("%d|%m|%y")
    if str(OT) <= str(SQLDATEALERT):
       while True: 
           await tbot.send_message(-1001158277850, "**ALERT**\n\n__Hello moderators please upgrade my SQL database for my proper functioning !\nSet a new DATABASE_URL__")
           await asyncio.sleep(5)
    

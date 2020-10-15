import asyncio
import datetime
import time
import pytz
from alexa import tbot, SQLDATEALERT
from telethon import events

loop = asyncio.get_event_loop()

async def check_dbb():
    LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    OT = LT.strftime("%d|%m|%y")
    if str(OT) <= str(SQLDATEALERT):     
         while True:
           await tbot.send_message(-1001158277850, "**ALERT**\n\n__Hello moderators please upgrade my SQL database for my proper functioning !\nSet a new DATABASE_URL__")

future = loop.create_task(check_dbb())
loop.run_until_complete(future)

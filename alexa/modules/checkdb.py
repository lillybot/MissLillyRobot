import asyncio
import datetime
import time
import requests
import pytz
from alexa import SQLDATEALERT, TOKEN

LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
OT = LT.strftime("%d/%m/%y")
if str(OT) <= str(SQLDATEALERT):     
   while True:
     url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=-1001233306063&text=*ALERT*\n\n_Hello moderators please upgrade my SQL database for my proper functioning  !\nSet a new DATABASE URL_&parse_mode=markdown'
     requests.post(url)
     time.sleep(5)

import threading

from alexa.modules.sql import BASE, SESSION
from sqlalchemy import (Boolean, Column, Integer, String, UnicodeText, distinct,
                        func)


class APPROVED(BASE):
    __tablename__ = "approvesystem"

    user_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = str(chat_id)
        
            
APPROVED.__table__.create(checkfirst=True)
APPROVE_INSERTION_LOCK = threading.RLock()

def approve_user(user_id, chat_id):
    with APPROVE_INSERTION_LOCK:
        approved_user = SESSION.query(APPROVED).get((user_id, str(chat_id)))
        if not approved_user:
            approved_user = APPROVED(user_id, str(chat_id))

        SESSION.add(approved_user)
        SESSION.commit()

def disapprove_user(user_id, chat_id):
    with APPROVE_INSERTION_LOCK:
        approved_user = SESSION.query(APPROVED).get((user_id, str(chat_id)))
        if not approved_user:
            return
        SESSION.delete(approved_user)
        SESSION.commit()

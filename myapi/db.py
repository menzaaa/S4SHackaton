from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import DB_URI
from models import User

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)

def seed():
    userlist = [
        User(name='max', password='password'),
        User(name='menno', password='pw'),
        User(name='robbert', password='robbert is met dubbel b')
    ]

    for user in userlist:
        print(user)
        session.add(user)

    session.commit()

seed()


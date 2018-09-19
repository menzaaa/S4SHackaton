from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import DB_URI
from models import User, Answer, Question

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
    questionlist = [
        Question(question='when did 9/11 happen?', answer='last year'),
        Question(question='is git a programming language?', answer='yes definitly')
    ]
    answerlist = [
        Answer(answer='test1', user_id = 1, question_id = 1),
        Answer(answer='test2', user_id = 1, question_id = 1),
        Answer(answer='test3', user_id = 1, question_id = 2),
    ]

    for user in userlist:
        session.add(user)

    for question in questionlist:
        session.add(question)

    for answer in answerlist:
        session.add(answer)

    session.commit()

seed()


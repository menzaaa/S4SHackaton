from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import DB_URI
from models import User, Answer, Question, Quiz, reset_db

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)

def seed():
    reset_db()

    userlist = [
        User(first_name='Max', last_name='HvA'),
        User(first_name='Menno', last_name='HvA'),
        User(first_name='Robert', last_name='HvA')
    ]

    for user in userlist:
        user.hash_password('qwerty')

    quizlist = [
        Quiz(name='My first time using JavaScript', user_id = 1),
        Quiz(name='JavaScript functions', user_id = 2)
    ]

    questionlist = [
        Question(name='Printing', description='Print out Hello World!', answer='Hello World!', quiz_id = 1),
        Question(name='Adding up the numbers', description='Use your knowledge to add up the numbers 1 and 2', answer='3', quiz_id = 1),
        Question(name='Multiplying numbers', description='Multiply 5 by 4', answer='20', quiz_id = 1)
    ]

    answerlist = [
        Answer(input='console.log("Hello World!")', user_id = 1, question_id = 1),
        Answer(input='1+2', user_id = 1, question_id = 2),
        Answer(input='5*4', user_id = 1, question_id = 3),
    ]

    for user in userlist:
        session.add(user)

    session.commit()

    for quiz in quizlist:
        session.add(quiz)

    session.commit()

    for question in questionlist:
        session.add(question)

    session.commit()

    for answer in answerlist:
        session.add(answer)

    session.commit()


seed()


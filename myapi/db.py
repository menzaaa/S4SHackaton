from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import DB_URI
from models import User, Answer, Question, Quiz, QuizQuestion, reset_db

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)

def seed():
    reset_db()

    quizlist = [
        Quiz(name='quiz1', user_id = 1),
        Quiz(name='quiz2', user_id = 2)
    ]    
    questionlist = [
        Question(question='when did 9/11 happen?', answer='last year'),
        Question(question='is git a programming language?', answer='yes definitly')
    ]

    quizquestionlist = [
        QuizQuestion(quiz_id = 1, question_id = 1),
        QuizQuestion(quiz_id = 2, question_id = 1),
        QuizQuestion(quiz_id = 1, question_id = 2),
        QuizQuestion(quiz_id = 2, question_id = 2) 
    ]

    answerlist = [
        Answer(answer='test1', user_id = 1, question_id = 1),
        Answer(answer='test2', user_id = 1, question_id = 2),
        Answer(answer='test3', user_id = 2, question_id = 1),
    ]

    userlist = [
        User(username='max'),
        User(username='menno'),
        User(username='robbert')
    ]

    for user in userlist:
        user.hash_password('qwerty')
    
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

    session.commit()

    for quiz in quizlist:
        session.add(quiz)

    session.commit()

    for question in questionlist:
        session.add(question)

    session.commit()

    for quizquestion in quizquestionlist:
        session.add(quizquestion)

    session.commit()

    for answer in answerlist:
        session.add(answer)

    session.commit()


seed()


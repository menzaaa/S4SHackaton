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
        Quiz(name='quiz1', user_id = 52),
        Quiz(name='quiz2', user_id = 52)
    ]    
    questionlist = [
        Question(question='when did 9/11 happen?', answer='last year'),
        Question(question='is git a programming language?', answer='yes definitly')
    ]

    quizquestionlist = [
        QuizQuestion(quiz_id = 71, question_id = 130),
        QuizQuestion(quiz_id = 71, question_id = 131),
        QuizQuestion(quiz_id = 71, question_id = 132),
        QuizQuestion(quiz_id = 71, question_id = 133) 
    ]

    answerlist = [
        Answer(answer='test1', user_id = 52, question_id = 101),
        Answer(answer='test2', user_id = 52, question_id = 101),
        Answer(answer='test3', user_id = 52, question_id = 101),
    ]

    userlist = [
        User(username='max'),
        User(username='menno'),
        User(username='robbert')
    ]

    for user in userlist:
        user.hash_password('qwerty')
    
    # questionlist = [
    #     Question(question='when did 9/11 happen?', answer='last year'),
    #     Question(question='is git a programming language?', answer='yes definitly')
    # ]
    # answerlist = [
    #     Answer(answer='test1', user_id = 1, question_id = 1),
    #     Answer(answer='test2', user_id = 1, question_id = 1),
    #     Answer(answer='test3', user_id = 1, question_id = 2),
    # ]

    for user in userlist:
        session.add(user)

    for quiz in quizlist:
        session.add(quiz)

    for question in questionlist:
        session.add(question)

    for quizquestion in quizquestionlist:
        session.add(quizquestion)

    for answer in answerlist:
        session.add(answer)


    session.commit()

seed()


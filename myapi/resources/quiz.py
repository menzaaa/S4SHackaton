from models import Quiz, Question, QuizQuestion
from db import session

from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort

question_fields = {
    'id': fields.Integer,
    'question': fields.String,
    'answer': fields.String
}

quiz_questions = {
    'id': fields.Integer,
    'name': fields.String,
    'questions': fields.List(fields.Nested(question_fields))
}

quiz_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

quizzes = {}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument(    'user_id', type=int)

class QuizResource(Resource):
    @marshal_with(quiz_questions)
    def get(self, id):
        quiz = session.query(Quiz).filter(Quiz.id == id).first()
        if not quiz:
            abort(404, message="Quiz {} does not exist.".format(id))

        quiz_question_ids = session.query(QuizQuestion.question_id).filter(QuizQuestion.quiz_id == quiz.id)
        questions = session.query(Question).filter(Question.id.in_(quiz_question_ids)).all()
        
        d = dict()
        d['id'] = quiz.id
        d['name'] = quiz.name
        d['questions'] = questions

        return d

    @marshal_with(quiz_fields)
    def put(self, id):
        quiz = session.query(Quiz).filter(Quiz.id == id).first()
        if quiz is not None:
            parsed_args = parser.parse_args()
            for key, value in parsed_args.items():
                if parsed_args[key] is not None:
                    setattr(quiz, key, value)
            session.commit()
            return quiz
        return {"error": "User not found"}, 404

    def delete(self, id):
        quiz = session.query(Quiz).filter(Quiz.id == id).first()
        session.delete(quiz)
        session.commit()
        
class QuizListResource(Resource):
    @marshal_with(quiz_fields)
    def get(self):
        quizzes = session.query(Quiz).all()
        return quizzes

    def post(self):
        parsed_args = parser.parse_args()
        quiz = Quiz(name=parsed_args['name'], user_id=parsed_args['user_id'])
        
        session.add(quiz)
        session.commit()
        return quiz.name, 201


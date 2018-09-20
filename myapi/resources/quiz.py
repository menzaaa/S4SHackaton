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
parser.add_argument('task', type=str)

class QuizOverviewResource(Resource):
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


class QuizListResource(Resource):
    @marshal_with(quiz_fields)
    def get(self):
        quizzes = session.query(Quiz).all()
        return quizzes


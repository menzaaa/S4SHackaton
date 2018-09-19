from models import Question, Answer
from db import session

from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort

question_fields = {
    'id': fields.Integer,
    'question': fields.String,
    'answer': fields.String
}

answer_fields = {
    'id': fields.Integer,
    'answer': fields.String,
    'user_id': fields.Integer
}

questions = {}

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class QuestionResource(Resource):
    @marshal_with(question_fields)
    def get(self, id):
        question = session.query(Question).filter(Question.id == id).first()
        if not question:
            abort(404, message="Question {} does not exist.".format(id))
        return question


class QuestionListResource(Resource):
    @marshal_with(question_fields)
    def get(self):
        questions = session.query(Question).all()
        print (questions)
        return questions


class QuestionAnswersResource(Resource):
    @marshal_with(answer_fields)
    def get(self, id):
        question_id = session.query(Question).get(id)
        answers = session.query(Answer).filter(Answer.question_id == id).all()
        return answers

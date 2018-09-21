from models import Question, Answer
from db import session

from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort

question_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'answer': fields.String,
    'quiz_id': fields.Integer
}

answer_fields = {
    'id': fields.Integer,
    'input': fields.String,
    'user_id': fields.Integer,
    'question_id': fields.Integer
}

questions = {}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('description', type=str)
parser.add_argument('answer', type=str)
parser.add_argument('quiz_id', type=int)

class QuestionResource(Resource):
    @marshal_with(question_fields)
    def get(self, id):
        question = session.query(Question).filter(Question.id == id).first()
        if not question:
            abort(404, message="Question {} does not exist.".format(id))
        return question

    @marshal_with(question_fields)
    def put(self, id):
        question = session.query(Question).filter(Question.id == id).first()
        if question is not None:
            parsed_args = parser.parse_args()
            for key, value in parsed_args.items():
                if parsed_args[key] is not None:
                    setattr(question, key, value)
            session.commit()
            return question
        return {"error": "User not found"}, 404

    def delete(self, id):
        question = session.query(Question).filter(Question.id == id).first()
        session.delete(question)
        session.commit()


class QuestionListResource(Resource):
    @marshal_with(question_fields)
    def get(self):
        questions = session.query(Question).all()
        return questions

    @marshal_with(question_fields)
    def post(self):
        parsed_args = parser.parse_args()
        question = Question(name=parsed_args['name'],
                            description=parsed_args['description'],
                            answer=parsed_args['answer'],
                            quiz_id=parsed_args['quiz_id']
                            )
        
        session.add(question)
        session.commit()
        return question, 201


class QuestionAnswersResource(Resource):
    @marshal_with(answer_fields)
    def get(self, id):
        question_id = session.query(Question).get(id)
        answers = session.query(Answer).filter(Answer.question_id == id).all()
        return answers

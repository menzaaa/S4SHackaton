from models import Question, Answer
from db import session

from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort

answer_fields = {
    'id': fields.Integer,
    'input': fields.String,
    'user_id': fields.Integer,
    'question_id': fields.Integer
}

answers = {}

parser = reqparse.RequestParser()
parser.add_argument('input', type=str)
parser.add_argument('user_id', type=int)
parser.add_argument('question_id', type=int)

class AnswerResource(Resource):
    @marshal_with(answer_fields)
    def get(self, id):
        answer = session.query(Answer).filter(Answer.id == id).first()
        if not answer:
            abort(404, message="Answer {} does not exist.".format(id))
        return answer

    @marshal_with(answer_fields)
    def put(self, id):
        answer = session.query(Answer).filter(Answer.id == id).first()
        if answer is not None:
            parsed_args = parser.parse_args()
            for key, value in parsed_args.items():
                if parsed_args[key] is not None:
                    setattr(answer, key, value)
            session.commit()
            return answer
        return {"error": "Answer not found"}, 404

    def delete(self, id):
        answer = session.query(Answer).filter(Answer.id == id).first()
        session.delete(answer)
        session.commit()

class AnswerListResource(Resource):
    @marshal_with(answer_fields)
    def get(self):
        answers = session.query(Answer).all()
        return answers

    @marshal_with(answer_fields)
    def post(self):
        parsed_args = parser.parse_args()
        answer = Answer(input=parsed_args['input'],
                        user_id=parsed_args['user_id'],
                        question_id=parsed_args['question_id']
                        )
        
        session.add(question)
        session.commit()
        return answer, 201

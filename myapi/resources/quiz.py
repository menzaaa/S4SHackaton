from models import Question, Answer
from db import session

from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort

quiz_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

quiz_questions_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'questions': fields.List(fields.Nested(quiz_fields))
}

quizzes = {}

class QuizOverviewResource():
    @marshal_with(quiz_questions_fields)
    def getQuiz(self, id):
        quiz = session.query(Quiz).filter(Quiz.id == id).first()
        if not quiz:
            abort(404, message="Question {} does not exist.".format(id))

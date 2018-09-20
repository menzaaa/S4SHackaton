from models import User, Answer
from db import session

from flask import Flask, request, g
from flask_restful import Resource, reqparse, fields, marshal_with, abort

from resources.auth import self_only

# from flask_httpauth import HTTPBasicAuth

from resources.auth import auth
# auth = HTTPBasicAuth()

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password_hash': fields.String,
    'uri': fields.Url('user', absolute=True),
}

answer_fields = {
    'id': fields.Integer,
    'answer': fields.String,
    'user_id': fields.Integer
}

users = {}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)

class UserResource(Resource):
    # @auth.verify_password
    # def verify_password(username, password):
    #     user = session.query(User).filter_by(username = username).first()
    #     if not user or not user.verify_password(password):
    #         print("Nee man")
    #         return False
    #     g.user = user
    #     return True

    @self_only
    @auth.login_required
    @marshal_with(user_fields)
    def get(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User {} does not exist.".format(id))
        return user

        # return {id: users[id]}

    def delete(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User {} does not exist".format(id))
        session.delete(user)
        session.commit()
        return {}, 204

    @marshal_with(user_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        user = session.query(User).filter(User.id == id).first()
        user.hash_password(parsed_args['password'])
        session.add(User)
        session.commit()

        return user, 201
    
        # users[id] = request.form['data']
        # return {id: users[id]}

class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = session.query(User).all()
        return users

    @marshal_with(user_fields)
    def post(self):
        parsed_args = parser.parse_args()
        user = User(username=parsed_args['username'])
        user.hash_password(parsed_args['password'])
        session.add(user)
        session.commit()
        return user, 201

class UserAnswersResource(Resource):
    @marshal_with(answer_fields)
    def get(self, id):
        user_id = session.query(User).get(id)
        answers = session.query(Answer).filter(Answer.user_id == id).all()
        return answers
        
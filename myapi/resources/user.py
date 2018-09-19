from models import User
from db import session

from flask import Flask, request
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal_with
from flask_restful import abort

from werkzeug.security import generate_password_hash, check_password_hash

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'password': fields.String,
    'uri': fields.Url('user', absolute=True),
}

users = {}

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class UserResource(Resource):
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
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
        user.password = parsed_args['password']
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
        user = User(name=parsed_args['name'], password=parsed_args['password'])
        session.add(user)
        session.commit()
        return user, 201
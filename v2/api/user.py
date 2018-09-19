from flask import abort, g
from flask_restful import Resource, reqparse, marshal_with, fields

from v2.api import api, meta_fields
from v2.api.auth import self_only
from v2.models.user import User
from v2.helpers import paginate
from v2.extentions import auth

user_parser = reqparse.RequestParser()
user_parser.add_argument('username')
user_parser.add_argument('password')
user_parser.add_argument('email')
user_parser.add_argument('first_name')
user_parser.add_argument('last_name')


# Marshalled field definitions for user objects
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
}

# Marshalled field definitions for collections of user objects
user_collection_fields = {
    'items': fields.List(fields.Nested(user_fields)),
    'meta': fields.Nested(meta_fields),
}

class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, user_id=None, username=None):
        user = None
        if username is not None:
            user = User.get_by_username(username)
        else:
            user = User.get_by_id(user_id)
        
        if not user:
            abort(404)

        return user

    @auth.login_required
    @self_only
    @marshal_with(user_fields)
    def post(self, user_id=None, username=None):
        g.user.update(**user_parser.parse_args())
        return g.user
    
    @auth.login_required
    @self_only
    @marshal_with(user_fields)
    def delete(self, user_id=None, username=None):
        g.user.delete()
        return 204


class UserCollecrionResource(Resource):
    @marshal_with(user_collection_fields)
    @paginate()
    def get(self):
        users = User.query
        return users

    @marshal_with(user_collection_fields)
    def post(self):
        user = User.create(**user_parser.parse_args())
        return user, 201

api.add_resource(UserResource, 'user/<int:user_id>', 'users/<username>')
api.add_resource(UserCollecrionResource, '/users')
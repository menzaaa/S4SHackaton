from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from flask import g, jsonify

from db import session
from resources.auth import auth

from models import User


# parser = reqparse.RequestParser()
# parser.add_argument('username', type=str)
# parser.add_argument('password', type=str)
class LoginResource(Resource):

    @auth.login_required
    def get(self):
        print(g.user)
        token = g.user.generate_auth_token()
        return jsonify({'token' : token.decode('ascii') })

    # @auth.verify_password
    # def verify_password(username_or_token, password):
    #     user = User.verify_auth_token(username_or_token)
    #     if not user:
    #         user = session.query(User).filter_by(username = username_or_token).first()
    #         if not user or not user.verify_password(password):
    #             print("Nee man")
    #             return False
    #     g.user = user
    #     return True, user.generate_auth_token()

    # @auth.login_required
    # def get_auth_token(self):
    #     token = g.user.generate_auth_token()
    #     return jsonify({'token' : token.decode('ascii') })


    # def post(self):
    #     parsed_args = parser.parse_args()
    #     username = parsed_args['username']
    #     password = parsed_args['password']

    #     return self.verify_password('max', 'qwerty')

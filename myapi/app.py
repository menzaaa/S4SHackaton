from flask import Flask, request
from flask_restful import Resource, Api

from resources.user import UserResource
from resources.user import UserListResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/user/<string:id>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
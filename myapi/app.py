from flask import Flask, request
from flask_restful import Resource, Api

from resources.foo import Foo

app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, '/foo/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
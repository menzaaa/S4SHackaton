from flask import Flask, request
from flask_restful import Resource

foos = {}

class Foo(Resource):
    def get(self, id):
        return {id: foos[id]}
    def put(self, id):
        foos[id] = request.form['data']
        return {id: foos[id]}
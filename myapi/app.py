from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

from resources.user import UserResource, UserListResource, UserAnswersResource
from resources.question import QuestionResource, QuestionListResource, QuestionAnswersResource
from resources.quiz import QuizResource, QuizListResource
from resources.answer import AnswerResource, AnswerListResource
from resources.login import LoginResource
from resources import auth

app = Flask(__name__)
CORS(app)
app.config['APPLICATION_ROOT'] = '/api'

app.config['SECRET_KEY'] = 'geheime code'

api = Api(app)

api.add_resource(LoginResource, '/login', endpoint='login')

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')
api.add_resource(UserAnswersResource, '/users/<string:id>/answers', endpoint='user_answers')

api.add_resource(QuestionResource, '/questions/<string:id>', endpoint='question')
api.add_resource(QuestionListResource, '/questions', endpoint='questions')
api.add_resource(QuestionAnswersResource, '/questions/<string:id>/answers', endpoint='question endpo_answers')

api.add_resource(QuizResource, '/quizzes/<string:id>', endpoint='quiz')
api.add_resource(QuizListResource, '/quizzes', endpoint = 'quizzes')

api.add_resource(AnswerResource, '/answers/<string:id>', endpoint='answer')
api.add_resource(AnswerListResource, '/answers', endpoint='answers')

if __name__ == '__main__':
    app.run(debug=True)
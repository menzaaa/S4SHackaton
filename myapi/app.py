from flask import Flask, request
from flask_restful import Resource, Api

from resources.user import UserResource, UserListResource, UserAnswersResource
from resources.question import QuestionResource, QuestionListResource, QuestionAnswersResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')
api.add_resource(UserAnswersResource, '/users/<string:id>/answers', endpoint='user_answers')

api.add_resource(QuestionResource, '/questions/<string:id>', endpoint='question')
api.add_resource(QuestionListResource, '/questions', endpoint='questions')
api.add_resource(QuestionAnswersResource, '/questions/<string:id>/answers', endpoint='question endpo_answers')

api.add_resource(QuizOverviewResource, '/quiz/<string:id>', endpoint='quiz')
#api.add_resource(QuizListResource, 'quizzes', endpoint = quizzes)

if __name__ == '__main__':
    app.run(debug=True)
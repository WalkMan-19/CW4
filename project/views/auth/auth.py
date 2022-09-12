from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, code=200, as_list=True, description='OK')
    def post(self):
        """
        create new user
        """
        req_json = request.json

        if req_json.get('email') and req_json.get('password'):
            return user_service.create_user(email=req_json.get('email'), password=req_json.get('password')), 201
        else:
            return "", 401


@api.route('/login/')
class LoginView(Resource):
    def post(self):
        """
        login user
        """
        req_json = request.json
        if req_json.get('email') and req_json.get('password'):
            return user_service.check(email=req_json.get('email'), password=req_json.get('password')), 200
        else:
            return "", 401

    def put(self):
        """
        update token
        """
        req_json = request.json
        if req_json.get('access_token') and req_json.get('refresh_token'):
            return user_service.update_token(
                access_token=req_json.get('access_token'), refresh_token=req_json.get('refresh_token')), 200
        else:
            return "", 401

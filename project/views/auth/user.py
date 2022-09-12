from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class UsersViews(Resource):
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        """
        get all users
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        return user_service.get_user_by_token(token=token)

    @api.marshal_with(user, code=200, description='OK')
    def patch(self):
        """
        update partial
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        data = request.json
        return user_service.update_user(data=data, token=token)


@api.route('/password/')
class UserViews(Resource):
    @api.marshal_with(user, code=200, description='OK')
    def put(self):
        """
        update password
        """
        data = request.json
        token = request.headers["Authorization"].split("Bearer ")[-1]
        return user_service.update_password(data=data, token=token)

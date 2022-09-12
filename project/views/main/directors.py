from flask_restx import Resource, Namespace
from flask import request
from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser

api = Namespace('directors')


@api.route('/')
class DirectorsViews(Resource):
    @api.expect(page_parser)
    @api.marshal_with(director, as_list=True, code=200, description="OK")
    def get(self):
        """
        get all directors
        """
        return director_service.get_all(**page_parser.parse_args())

    def post(self):
        pass


@api.route('/<int:director_id>')
class DirectorViews(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(director, code=200, description="OK")
    def get(self, director_id: int):
        """
        get director by id
        """
        return director_service.get_item(pk=director_id)

    def put(self, director_id: int):
        pass

    def patch(self, director_id: int):
        pass

    def delete(self, director_id: int):
        pass

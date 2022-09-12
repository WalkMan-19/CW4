from flask_restx import Namespace, Resource
from flask import request
from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

api = Namespace("movies")


@api.route('/')
class MoviesViews(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description="OK")
    def get(self):
        """
        get all movies
        """

        status = request.args.get("status")

        return movie_service.get_all(filter=status, **page_parser.parse_args())

    def post(self):
        """
        add new movie
        """
        req_json = request.json
        pass


@api.route('/<int:movie_id>')
class MovieViews(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description="OK")
    def get(self, movie_id: int):
        """
        get movie by id
        """
        return movie_service.get_item(pk=movie_id)

    def put(self, movie_id: int):
        pass

    def patch(self, movie_id: int):
        pass

    def delete(self, movie_id: int):
        pass

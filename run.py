from project.config import config
from project.models import Genre
from project.server import create_app

app = create_app(config)


# @app.shell_context_processor
# def shell():
#    return {
#        "db": db,
#      "Genre": Genre,
#        "Movies": Movies,
#       "Directors": Directors,
#       "Users": Users,
#    }


if __name__ == '__main__':
    app.run(debug=True)

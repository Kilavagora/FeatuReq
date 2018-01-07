"""Routes"""
from datetime import datetime
from flask import Flask

from .config import app_config
from app.models import db
from app.errors import make_json_error
from .encoder import CustomJSONEncoder

from werkzeug.exceptions import default_exceptions


def create_app(config_name):
    """Create app endpoints"""
    from .views.category import cat
    from .views.client import cli
    from .views.feature import feat

    app = Flask(__name__, static_url_path="")

    for code in default_exceptions.keys():
        app.errorhandler(code)(make_json_error)

    app.json_encoder = CustomJSONEncoder

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app._static_folder = "../static"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(cat)
    app.register_blueprint(feat)
    app.register_blueprint(cli)

    @app.route('/', methods=['GET'])
    def root():
        return app.send_static_file("index.html")

    return app

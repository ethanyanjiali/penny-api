from flask import current_app, Flask
from flask_jwt import JWT
from .auth import authenticate, identity
from flask_cors import CORS
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import config


def get_config():
    config_name = os.getenv('FLASK_ENV', 'production')
    if config_name == 'production':
        return config.ProductionConfig
    else:
        return config.DevelopmentConfig


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(get_config())
    app.config.from_pyfile('flask.cfg')

    jwt = JWT(app, authenticate, identity)

    from .routes.user_route import user
    app.register_blueprint(user)

    from .routes.event_route import event
    app.register_blueprint(event)

    from .routes.common_route import common
    app.register_blueprint(common)

    CORS(app)

    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["2 per second"],
    )

    return app
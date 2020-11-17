from flask import Flask
from flask_cors import CORS
# from .database.database import engine, Base

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    # Base.metadata.create_all(engine)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    with app.app_context():

        # from . import guestbook
        # app.register_blueprint(guestbook.bp)

        from . import github
        app.register_blueprint(github.bp)

    print("!!!!! SERVER START !!!!!")

    github.get_github_test()

    return app

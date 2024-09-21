from flask import Flask
from app.routes import bp_product


def initialize_app():
    app = Flask(__name__)
    app.register_blueprint(bp_product)
    return app

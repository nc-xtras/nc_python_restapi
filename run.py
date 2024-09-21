from flask import Flask
from app.routes import bp_product

app = Flask(__name__)

app.register_blueprint(bp_product)


if __name__ == "__main__":
    app.run(debug=True)

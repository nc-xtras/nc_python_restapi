from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask REST API!"


@app.route("/api/items", methods=["GET"])
def get_items():
    items = [
        {"id": 1, "name": "Item 1", "description": "First item"},
        {"id": 2, "name": "Item 2", "description": "Second item"},
    ]
    return {"items": items}


@app.route("/api/items", methods=["POST"])
def create_item():
    new_item = request.get_json()  # Get the new item from the request body
    return {"item": new_item}, 201  # Return 201 status to indicate creation


if __name__ == "__main__":
    app.run(debug=True)

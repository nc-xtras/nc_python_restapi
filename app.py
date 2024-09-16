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


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    items = [
        {"id": 1, "name": "Item 1", "description": "First item"},
        {"id": 2, "name": "Item 2", "description": "Second item"},
    ]
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return {"item": item}
    else:
        return {"message": "Item not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)

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
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return {"item": item}
    else:
        return {"message": "Item not found"}, 404


@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_item = request.get_json()
    return {"message": f"Item {item_id} updated", "item": updated_item}


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    return {"message": f"Item {item_id} deleted"}


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "First item"},
    {"id": 2, "name": "Item 2", "description": "Second item"},
]


@app.route("/")
def home():
    return "Welcome to the Flask REST API!"


@app.route("/api/items", methods=["GET"])
def get_items():
    return {"items": items}


@app.route("/api/items", methods=["POST"])
def create_item():
    new_item = request.get_json()  # Get the new item from the request body
    items.append(new_item)
    return {"item": new_item}, 201  # Return 201 status to indicate creation


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return {"item": item}
    else:
        return {"message": "Item not found"}, 404


@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_item = request.get_json()
    item = next((item for item in items if item["id"] == item_id), None)

    if item:
        # Perbarui atribut item yang ada
        item["name"] = updated_item.get("name", item["name"])
        item["description"] = updated_item.get("description", item["description"])
    return {"message": f"Item {item_id} updated", "item": item}


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        items.remove(item)
    return {"message": f"Item {item_id} deleted"}


if __name__ == "__main__":
    app.run(debug=True)

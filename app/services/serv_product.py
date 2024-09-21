products = [
    {"id": 1, "name": "product 1", "description": "First product", "price": 1000},
    {"id": 2, "name": "product 2", "description": "Second product", "price": 2000},
]


class ServProduct:
    @staticmethod
    def get_products():
        return {"data": products}

    @staticmethod
    def create_product(new_product):
        products.append(new_product)
        return {"data": new_product}, 201  # Return 201 status to indicate creation

    def get_product_by_id(product_id: int):
        product_by_id = next((p for p in products if p["id"] == product_id), None)
        if product_by_id:
            return {"data": product_by_id}
        else:
            return {
                "message": "Product not found"
            }, 404  # Return 400 to indicate no item found

    @staticmethod
    def update_product(product_id: int, updated_product):
        product_to_update = next((p for p in products if p["id"] == product_id), None)

        if product_to_update:
            # Perbarui atribut item yang ada
            product_to_update["name"] = updated_product.get(
                "name", product_to_update["name"]
            )
            product_to_update["description"] = updated_product.get(
                "description", product_to_update["description"]
            )
            product_to_update["price"] = updated_product.get(
                "price", product_to_update["price"]
            )
        return {"message": f"Product {product_id} updated", "data": product_to_update}

    @staticmethod
    def delete_product(product_id: int):
        product_to_delete = next((p for p in products if p["id"] == product_id), None)
        if product_to_delete:
            products.remove(product_to_delete)
        return {"message": f"Product {product_id} deleted"}

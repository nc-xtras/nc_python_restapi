from app.mocks import MockProduct
from app.utils import ResponseCode


class ServProduct:
    @staticmethod
    def get_products():
        return ResponseCode.success_ok(data=MockProduct.products)

    @staticmethod
    def create_product(new_product):
        MockProduct.products.append(new_product)
        return ResponseCode.success_created(data=new_product)

    @staticmethod
    def get_product_by_id(product_id: int):
        product_by_id = next(
            (p for p in MockProduct.products if p["id"] == product_id), None
        )
        if product_by_id:
            return ResponseCode.success_ok(data=product_by_id)
        else:
            return ResponseCode.error_not_found()

    @staticmethod
    def update_product(product_id: int, updated_product):
        product_to_update = next(
            (p for p in MockProduct.products if p["id"] == product_id), None
        )

        if product_to_update:
            product_to_update["name"] = updated_product.get(
                "name", product_to_update["name"]
            )
            product_to_update["description"] = updated_product.get(
                "description", product_to_update["description"]
            )
            product_to_update["price"] = updated_product.get(
                "price", product_to_update["price"]
            )
            return ResponseCode.success_ok(data=updated_product)
        else:
            return ResponseCode.error_not_found()

    @staticmethod
    def delete_product(product_id: int):
        product_to_delete = next(
            (p for p in MockProduct.products if p["id"] == product_id), None
        )
        if product_to_delete:
            MockProduct.products.remove(product_to_delete)
            return ResponseCode.success_ok()
        else:
            return ResponseCode.error_not_found()

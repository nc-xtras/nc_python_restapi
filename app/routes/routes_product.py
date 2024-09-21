from flask import Blueprint, request
from app.services import ServProduct

# * blueprint is solution for error "app not defined"
bp_product = Blueprint("product", __name__)


@bp_product.route("/")
def home():
    return "Welcome to the Flask REST API!"


@bp_product.route("/products", methods=["GET"])
def get_products():
    return ServProduct.get_products()


@bp_product.route("/products", methods=["POST"])
def create_product():
    return ServProduct.create_product(request.json)


@bp_product.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    return ServProduct.get_product_by_id(product_id)


@bp_product.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    return ServProduct.update_product(
        product_id=product_id, updated_product=request.json
    )


@bp_product.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return ServProduct.delete_product(product_id)

from flask import Blueprint, request, Response
import simplejson as json
import sqlite3

from api.repositories import ProductRepository
from api.utilities import ProductMapper


CONTENT_TYPE_APPLICATION_JSON = 'application/json'

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/')
def index():
    return 'Hello, world!'

@product_controller.route('/products', methods=['GET'])
def get_all_products():
    products = ProductRepository.get_all_products()
    products_json = ProductMapper.convert_to_json(products)
    return Response(products_json, 200, content_type=CONTENT_TYPE_APPLICATION_JSON)

@product_controller.route('/products/<id>', methods=['GET'])
def get_product_by_id(id):
    product = ProductRepository.get_product_by_id(id)
    product_json = ProductMapper.convert_to_json(product)
    return Response(
        product_json, 200 if product_json else 404,
        content_type=CONTENT_TYPE_APPLICATION_JSON
    )

@product_controller.route('/products', methods=['POST'])
def add_product():
    product_dict = request.json
    product = ProductMapper.convert_to_object(product_dict)
    new_product = ProductRepository.add_product(product)
    return Response(new_product, 201, content_type=CONTENT_TYPE_APPLICATION_JSON)

@product_controller.route('/products/<id>', methods=['PUT'])
def update_product_by_id(id):
    product_dict = request.json
    new_product = ProductRepository.update_product_by_id(id, product_dict)
    return Response(new_product, 200, content_type=CONTENT_TYPE_APPLICATION_JSON)

@product_controller.route('/products/<id>', methods=['DELETE'])
def remove_product_by_id(id):
    ProductRepository.remove_product_by_id(id)
    return Response(None, 204, content_type=CONTENT_TYPE_APPLICATION_JSON)


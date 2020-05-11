import sqlite3

from api.configuration import Configuration
from api.exceptions import ResourceNotFoundError
from api.models import Product


db = Configuration.get_db()

class ProductRepository:
    
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(id):
        product = Product.query.get(id)
        if product is None:
            raise ResourceNotFoundError('Product with id {id} does not exist.')
        return product

    @staticmethod
    def add_product(product):
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_product_by_id(id, product_dict):
        retrieved_products = Product.query.filter_by(id=id)
        if retrieved_products.first() is None:
            raise ResourceNotFoundError('Product with id {id} does not exist.')
        retrieved_products.update(product_dict)
        db.session.commit()

    @staticmethod
    def remove_product_by_id(id):
        Product.query.filter_by(id=id).delete()

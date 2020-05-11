from unittest import TestCase
from unittest.mock import patch

from api.exceptions import ResourceNotFoundError
from api.models import Product
from api.repositories import ProductRepository


class ProductRepositoryTest(TestCase):

    @patch('api.repositories.product_repository.Product.query')
    def test_get_all_products_should_return_all_products(self, query_mock):
        product = Product()
        query_mock.all.return_value = [product]

        result = ProductRepository.get_all_products()

        query_mock.all.assert_called_with()
        self.assertEqual(result, [product])

    @patch('api.repositories.product_repository.Product.query')
    def test_get_product_by_id_should_raise_error_when_the_product_does_not_exist(self, query_mock):
        query_mock.get.return_value = None
        
        with self.assertRaises(ResourceNotFoundError):
            result = ProductRepository.get_product_by_id(1)

    @patch('api.repositories.product_repository.Product.query')
    def test_get_product_by_id_should_return_a_product(self, query_mock):
        query_mock.get.return_value = product = Product()
        
        result = ProductRepository.get_product_by_id(1)

        self.assertEqual(result, product)


if __name__ == '__main__':
    unittest.main()

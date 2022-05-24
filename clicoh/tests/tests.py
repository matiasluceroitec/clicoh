import pytest
import requests

from ecommerce.repository import ProductRepository
from factories import ProductFactory

@pytest.mark.django_db
def test_get_all_products():
    product_1 = ProductFactory(id='Fut1', name='Product 1', stock=10, price=10)
    product_2 = ProductFactory(id='Fut2', name='Product 2', stock=20, price=14)

    product_repository = ProductRepository()
    assert len(product_repository.get_all())

@pytest.mark.django_db
def test_update_stock_product():
    product_1 = ProductFactory(id='Fut1', name='Product 1', stock=10, price=10)
    product_repository = ProductRepository()
    product_repository.update_stock_a_product(product_1.id, 20)
    assert product_repository.get_stock_a_product(product_1.id) == 20

@pytest.mark.django_db
def test_get_all_endpoint():
    response = requests.get('http://localhost:8000/products/products/')

    assert response.status_code == 200

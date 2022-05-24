import factory

from ecommerce.models import Product, Order, OrderDetail


class ProductFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Product
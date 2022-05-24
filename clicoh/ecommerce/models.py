import requests
from decimal import Decimal
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)

    def get_total(self):
        total = 0
        order_detail = OrderDetail.objects.filter(order_id=self.id)
        for detail in order_detail:
            total += detail.quantity * detail.product.price
        return total

    def get_total_usd(self):
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        response = requests.get(url)
        data = response.json()
        for casa in data:
            if casa['casa']['nombre'] == "Dolar Blue":
                return self.get_total() * Decimal(casa['casa']['venta'].replace(',', '.'))

    def get_order_details(self):
        print("****", self.id)
        return OrderDetail.objects.filter(order_id=self.id)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return str(self.order.id)

    def save(self, *args, **kwargs):
        product = Product.objects.get(id=self.product.id)
        product.stock = product.stock - self.quantity
        product.save()
        super().save(*args, **kwargs)


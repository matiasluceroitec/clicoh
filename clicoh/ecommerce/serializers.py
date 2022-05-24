from rest_framework import serializers

from .models import Order, OrderDetail, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock')
        

class OrderSerializer(serializers.ModelSerializer):
    get_total = serializers.SerializerMethodField()
    get_total_usd = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('date', 'get_total', 'get_total_usd',)

    def get_total(self, obj) -> float:
        return obj.get_total()

    def get_total_usd(self, obj) -> float:
        return obj.get_total_usd()

    

class OrderDetailForOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetail
        fields = ('quantity', 'product', 'order')


    def validate_quantity(self, value):
        if value <= 0:
            raise ValueError('Quantity can not be zero or negative')
        return value

    def validate_product(self, value):
        orders_detail = OrderDetail.objects.filter(order=self.context['order'])
        # TODO refactor this when methods is put or patch
        for product in orders_detail:
            if value == product.product:
                raise ValueError('Ya existe el product')
        return value


class OrderDetailSerializer(serializers.ModelSerializer):
    orders = OrderDetailForOrderSerializer(many=True, required=False)
    
    class Meta:
        model = Order
        fields = ('date' ,'get_total', 'get_total_usd', 'orders',)

    def get_total(self, obj) -> float:
        return obj.get_total()

    def get_total_usd(self, obj) -> float:
        return obj.get_total_usd()

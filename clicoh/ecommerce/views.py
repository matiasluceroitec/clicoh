from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Order, OrderDetail, Product
from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer, OrderDetailForOrderSerializer
from .repository import OrderRepository, ProductRepository


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        product = self.get_object().id
        stock = request.data.get('stock')
        
        product_repository = ProductRepository()
        try:
            product_update = product_repository.update_stock_a_product(
                product, stock
            )
            return Response(self.serializer_class(product_update).data)
        except Exception as e:
            return Response(self.serializer_class.errors)


class OrderViewSet(viewsets.ModelViewSet):
    permissions_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order_repository = OrderRepository()
        order_repository.delete(order.id)
        return Response(self.serializer_class(order).data)


class OrderDetailViewSet(viewsets.ModelViewSet):
    permissions_classes = [IsAuthenticated]
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailForOrderSerializer

    def create(self, request):
        order_serializer = self.serializer_class(data = request.data, context = request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data)
        else:
            return Response(order_serializer.errors, status_code=404)

    def partial_update(self, request, *args, **kwargs):
        order_detail = self.get_object()

        order_detail.quantity = request.data.get('quantity')
        order_serializer = self.serializer_class(data = request.data, context = request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data)
        else:
            return Response(order_serializer.errors, status_code=404)
    

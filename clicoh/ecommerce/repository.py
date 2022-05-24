from .models import Product, Order, OrderDetail

class ProductRepository:
    def get_all(self):
        return Product.objects.all()
    
    def get_stock_a_product(self, product_id):
        return Product.objects.get(id=product_id).stock

    def restore_stock_a_product(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        product.stock = product.stock + quantity
        product.save()
        return product

    def update_stock_a_product(self, product_id, stock):
        product = Product.objects.get(id=product_id)
        product.stock = stock
        product.save()
        return product
    
    def less_stock_a_product(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        product.stock = product.stock - quantity
        product.save()
        return product
    
    def verify_stock_a_product(self, product_id, quantity):
        current_stock = self.get_stock_a_product(product_id)
        if current_stock >= quantity:
            return self.less_stock_a_product(product_id, quantity)
        else:
            raise Exception('No hay stock suficiente')

        
class OrderRepository:
    def get_all(self):
        return Order.objects.all()

    def delete(self, order_id):
        order_detail_repository = OrderDetailRepository()
        order_detail = order_detail_repository.get_a_detail_by_order(
            order_id
        )
        for od in order_detail:
            order_detail_repository.deleted_a_order_detail_restore_stock(
                od.id
            )
        order = Order.objects.get(id=order_id)
        order.delete()
        return self.get_all()


class OrderDetailRepository:
    def get_all(self):
        return OrderDetail.objects.all()

    def get_a_detail_by_order(self, order_id):
        return OrderDetail.objects.filter(order_id=order_id).all()

    def delete(self, order_detail_id):
        try:
            OrderDetail.objects.get(id=order_detail_id).delete()
        except Exception as e:
            return e

    def get_products_on_order_detail(self, order_detail_id):
        return OrderDetail.objects.filter(
            id=order_detail_id
        ).all().values('product_id', 'quantity')

    def deleted_a_order_detail_restore_stock(self, order_detail_id):
        product_repository = ProductRepository()

        products = self.get_products_on_order_detail(order_detail_id)
        for product in products:
            product_repository.restore_stock_a_product(
                product['product_id'], product['quantity']
            )
        self.delete(order_detail_id)

        return self.get_all()
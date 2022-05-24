from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderDetailViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orders_detail', OrderDetailViewSet)

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('products', views.ProductViewSet, basename='products')

urlpatterns = router.urls

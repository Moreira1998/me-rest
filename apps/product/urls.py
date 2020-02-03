from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.viewsets import CategoryViewSet, BrandViewSet, StateViewSet
from apps.product.viewsets import PriceViewSet, ProductViewSet

urlpatterns = []

routers = DefaultRouter()
routers.register(r'p'
                 r'', ProductViewSet)
routers.register(r'category', CategoryViewSet)
routers.register(r'brand', BrandViewSet)
routers.register(r'state', StateViewSet)
routers.register(r'price', PriceViewSet)

urlpatterns += routers.urls

from django.urls import path, include
from apps.store.viewsets import StoreViewSet
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
routers.register(r'', StoreViewSet)


urlpatterns = [
    path('', include(routers.urls)),

]
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from orders.views import *
router = routers.DefaultRouter()
router.register(r'table',TableViewSet)
router.register(r'order',OrderViewSet)
router.register(r'product',ProductViewSet)
router.register(r'custom',CustomizationViewSet)
router.register(r'orderItem',OrderItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/" , include(router.urls)),
]
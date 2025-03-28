from rest_framework import viewsets
from .serializers import *
from .models import *

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomizationCategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomizationCategory.objects.all()
    serializer_class = CustomizationCategorySerializer


class CustomizationViewSet(viewsets.ModelViewSet):
    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

def drop_orders_product_table():
    from django.db import connection
    with connection.cursor() as cursor:
        if connection.vendor == 'postgresql':
            cursor.execute("DROP TABLE IF EXISTS orders_product CASCADE;")
        else:
            cursor.execute("DROP TABLE IF EXISTS orders_product;")

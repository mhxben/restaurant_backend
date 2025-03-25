from rest_framework import serializers
from .models import *


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CustomizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customization
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    customizations = CustomizationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    customizations = CustomizationSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

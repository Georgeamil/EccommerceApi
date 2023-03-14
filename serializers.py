from rest_framework import serializers
from customer.models import Customer, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','customer', 'description', 'price', 'is_active', 'created_at')

class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'address', 'created_at', 'products')

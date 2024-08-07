# products/serializers.py
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price','quantity','category']

    def validate_quantity(self, value):
        if value > 100:
            raise serializers.ValidationError("Quantity cannot exceed 100.")
        return value

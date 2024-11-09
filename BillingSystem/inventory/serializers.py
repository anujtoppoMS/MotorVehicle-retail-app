from rest_framework import serializers
from .models import Product, ProductModel, ProductColour, ProductPrice

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class ProductColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColour
        fields = '__all__'

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = '__all__'
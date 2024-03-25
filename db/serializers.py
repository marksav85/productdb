from rest_framework import serializers
from .models import Product, SubCategory, SubProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProduct
        fields = '__all__'


from rest_framework import generics
from .models import Product, SubCategory, SubProduct
from .serializers import ProductSerializer, SubCategorySerializer, SubProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubProductList(generics.ListCreateAPIView):
    queryset = SubProduct.objects.all()
    serializer_class = SubProductSerializer

class SubProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubProduct.objects.all()
    serializer_class = SubProductSerializer
# Create your models here.
from django.db import models

class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=100)

class SubCategory(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    subCategoryId = models.IntegerField()
    subCategoryName = models.CharField(max_length=100)

class SubProduct(models.Model):
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    subProductId = models.IntegerField()
    subProductName = models.CharField(max_length=100)
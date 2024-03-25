from django.db import models

class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=100)

class SubCategory(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    subCategoryId = models.IntegerField(primary_key=True)
    subCategoryName = models.CharField(max_length=100)

class SubProduct(models.Model):
    subCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    subProductId = models.IntegerField(primary_key=True)
    subProductName = models.CharField(max_length=100)
    
class OrderList(models.Model):
    # Convert products, subcategories, and subproducts to JSONField
    products = models.JSONField(null=True)  
    subcategories = models.JSONField(null=True)  
    subproducts = models.JSONField(null=True)
    

import json
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productdb.settings')

# Initialize Django
django.setup()

# Import your Django models after Django is initialized
from db.models import Product, SubCategory, SubProduct

def load_data():

    Product.objects.all().delete()
    SubCategory.objects.all().delete()
    SubProduct.objects.all().delete()
    with open('products_db.json') as f:
        data = json.load(f)

    # Populate products
    for product_data in data['products']:
        product = Product.objects.create(productId=product_data['productId'], productName=product_data['productName'])
        
    # Populate subcategories
    for subcategory_data in data['subcategories']:
        product = Product.objects.get(productId=subcategory_data['productId'])
        subcategory = SubCategory.objects.create(productId=product, subCategoryId=subcategory_data['subCategoryId'], subCategoryName=subcategory_data['subCategoryName'])
    
    # Populate subproducts
    for subproduct_data in data['subproducts']:
        subcategory = SubCategory.objects.get(subCategoryId=subproduct_data['subCategoryId'])
        subproduct = SubProduct.objects.create(subCategoryId=subcategory, subProductId=subproduct_data['subProductId'], subProductName=subproduct_data['subProductName'])
    pass

if __name__ == "__main__":
    load_data()

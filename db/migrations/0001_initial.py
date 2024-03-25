# Generated by Django 5.0.3 on 2024-03-24 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryId', models.IntegerField()),
                ('subCategoryName', models.CharField(max_length=100)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.product')),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subProductId', models.IntegerField()),
                ('subProductName', models.CharField(max_length=100)),
                ('subCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.subcategory')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-22 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='commentable',
            field=models.BooleanField(default=True),
        ),
    ]

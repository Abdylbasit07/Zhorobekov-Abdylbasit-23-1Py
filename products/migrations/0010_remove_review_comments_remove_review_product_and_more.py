# Generated by Django 4.1.4 on 2023-01-03 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_product_commentable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

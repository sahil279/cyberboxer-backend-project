# Generated by Django 3.0.1 on 2019-12-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_image',
            field=models.ImageField(default='default.jpg', upload_to='product_images'),
        ),
    ]
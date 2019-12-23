# Generated by Django 3.0.1 on 2019-12-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter the name of the product', max_length=30)),
                ('product_description', models.CharField(help_text='explain about the product', max_length=256)),
                ('quantity', models.IntegerField()),
                ('Product_image', models.ImageField(default='default.jpg', upload_to='product_image')),
            ],
        ),
    ]
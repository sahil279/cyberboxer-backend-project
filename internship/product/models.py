from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30,help_text="enter the name of the product")
    product_description = models.CharField(max_length=256,help_text='explain about the product')
    quantity = models.IntegerField()
    Product_image = models.ImageField( default='default.jpg',upload_to='product_images')

    def __str__(self):
        return self.name

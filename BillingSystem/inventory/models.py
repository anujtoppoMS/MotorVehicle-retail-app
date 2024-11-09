from django.db import models
from datetime import date

class Product(models.Model):
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=100, default=None)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

class ProductModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    year_of_make = models.DateField(default=date.today)
    serial_number = models.CharField(max_length=100, unique=True)
    chassis_number = models.CharField(max_length=100, unique=True)
    capacity = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100, unique=True)
    battery_number = models.CharField(max_length=100, unique=True)
    key_number = models.CharField(max_length=100, unique=True)
    sales_status=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class ProductColour(models.Model):
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='colours')
    colour_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_model.name} - {self.colour_name}"

class ProductPrice(models.Model):
    product_colour = models.ForeignKey(ProductColour, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_colour.colour_name} - {self.price}"

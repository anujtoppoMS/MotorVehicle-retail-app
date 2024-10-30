from typing import Any
from django.db import models
from django.db.models import UniqueConstraint
from datetime import date
from inventory.models import Product, ProductModel,ProductColour,ProductPrice

class Sales_Invoice(models.Model):
    Invoice_number=models.CharField(max_length=20, unique=True, verbose_name='Invoice ID')
    Make_and_model=models.CharField(max_length=20, default=None)
    Serial_number=models.CharField(max_length=15, unique=True)
    Chasis_number=models.CharField(max_length=15, unique=True)
    Engine_number=models.CharField(max_length=15, unique=True)
    Battery_number=models.CharField(max_length=15, unique=True)
    Key_number=models.CharField(max_length=15, unique=True)
    Customer_name=models.CharField(max_length=15, default=None)
    Customer_id=models.CharField(max_length=15, default=None)
    customer_address=models.TextField(default=None)
    cust_contact=models.PositiveIntegerField(default=None)
    Sales_agent=models.CharField(max_length=15, default=None)
    Date_of_sale=models.DateField(default=date.today)
    Payment_reference_no=models.CharField(max_length=20, default=None, null=True, verbose_name="Payment Reference No.")
    Price_break = models.PositiveIntegerField(default=None, null=True, verbose_name="Price")
    Sold_status=models.BooleanField(default=False, verbose_name='Sale status')

    def __str__(self):
        return self.Invoice_number


class customer_details(models.Model):
    Name=models.CharField(max_length=20, verbose_name='Name')
    Email=models.EmailField(unique=True, verbose_name='email')
    Contact=models.PositiveIntegerField(verbose_name='Contact Number')
    Address=models.TextField(max_length=120, verbose_name='Address')
    Identification=models.CharField(max_length=10, verbose_name='Gov ID')
    ID_number=models.CharField(max_length=10, verbose_name='ID Number')
    Payment_mode=models.CharField(max_length=20, verbose_name='Payment Mode')
    class Meta:
        constraints = [ UniqueConstraint(fields=['Name', 'Email', 'Contact'], name='unique_customer')]

    def __str__(self) -> str:
        return f'{self.Name} - {self.Contact}'

class customer_sales(models.Model):
    customer_details=models.ForeignKey(customer_details, on_delete=models.CASCADE, related_name='cust_name', default=None)
    Name_agent=models.CharField(max_length=15)
    Email=models.EmailField()
    Contact=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.customer_details.Name}'


class Stockview(Product):
    def __init__(self, id) -> None:
        self.id=id
        self.obj=Product.objects.get(id=self.id)
        self.model_obj=self.obj.models.all()

    def __str__(self):
        return f'{self.model_obj.values()}'
         

    

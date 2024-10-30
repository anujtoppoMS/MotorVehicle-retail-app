from django import forms
from .models import Product, ProductModel, ProductColour, ProductPrice

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'model_type', 'status']

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product','name', 'year_of_make', 'serial_number', 'chassis_number', 'capacity', 'engine_number', 'battery_number', 'key_number']

class ProductColourForm(forms.ModelForm):
    class Meta:
        model = ProductColour
        fields = ['colour_name']

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['price']

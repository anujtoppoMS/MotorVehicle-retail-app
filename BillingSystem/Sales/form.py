from django import forms
from inventory.models import ProductModel, ProductPrice
from .models import customer_details, customer_sales, Sales_Invoice
from django.core.exceptions import ValidationError

class SalesForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product']

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['product_colour']

class customer_details_form(forms.ModelForm):
    class Meta:
        model = customer_details
        fields = ['Name', 'Email', 'Contact', 'Identification', 'ID_number', 'Address', 'Payment_mode']

    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data.get('Name')
        email=cleaned_data.get('Email')
        number=cleaned_data.get('Contact')

        if customer_details.objects.filter(Name=name, Email=email, Contact=number).exists():
            raise ValidationError('A customer with this name, number and email already exists !!')
        return cleaned_data
    
class customer_sales_form(forms.ModelForm):
    class Meta:
        model = customer_sales
        fields = ['customer_details', 'Name_agent']

class Generate_bill_quote(forms.Form):
    Invoice_number=forms.CharField(max_length=20)

class Generate_invoice(forms.Form):
    Invoice_number=forms.CharField(max_length=20)
    Payment_reference_no=forms.CharField(max_length=20)

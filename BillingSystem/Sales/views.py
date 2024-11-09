from django.shortcuts import render,redirect
from inventory.models import ProductPrice, ProductModel
from .models import customer_details,Sales_Invoice
from .form import SalesForm, ProductPriceForm, customer_details_form, customer_sales_form, Generate_bill_quote, Generate_invoice
from django.contrib import messages
from .logics import filter_output
from .html2pdf import html_to_pdf
from django.contrib.auth.decorators import login_required

# import requests

# response = requests.get('http://127.0.0.1:8000/inventory/get_product/')

# print(response.text)

# ---------------------------------------------------------------------- start of available stock view -------------------------------------------------------------------------------------------
@login_required
def stocks(request):
    if request.method == 'POST':
        saleform=SalesForm(request.POST)
        colourform=ProductPriceForm(request.POST)
        customerform=customer_sales_form(request.POST)
        if saleform.is_valid() and colourform.is_valid() and customerform.is_valid():
              name=saleform.cleaned_data['product']
              color=colourform.cleaned_data['product_colour']
              customer=customerform.cleaned_data['customer_details']
              sales_agent=customerform.cleaned_data['Name_agent']
            #   print(name,color,customer,sales_agent)
              obj=filter_output(name,color,customer, sales_agent)
              obj.filter_data()
              print('here', obj )
              return redirect('stocks')
    else:
          saleform=SalesForm()
          colourform=ProductPriceForm()
          customerform=customer_sales_form()
    data_list2 = ProductPrice.objects.all()
    list_data=[]
    for first in data_list2:
            list_data.append({'Product':first.product_colour.product_model.product.name, 'Product_Model':first.product_colour.product_model, 'Name':first.product_colour.product_model.name, 'Make':first.product_colour.product_model.year_of_make, 'SN':first.product_colour.product_model.serial_number, 
                            'Chassis_No':first.product_colour.product_model.chassis_number, 'Capacity':first.product_colour.product_model.capacity, 'Engine_No':first.product_colour.product_model.engine_number, 
                            'Battery_No':first.product_colour.product_model.battery_number, 'Key_No':first.product_colour.product_model.key_number, 'Colour':first.product_colour.colour_name, 'Price':first.price})
    context = {
        'context_data': list_data,
        'salesform' : saleform,
        'colourform' : colourform,
        'customerform' : customerform
    }        
    return render(request, 'frontend/stocks.html', context)

# ---------------------------------------------------------------------- end of available stock view -------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------- start of customer registration view -------------------------------------------------------------------------------------------

@login_required
def customer_reg(request):
    if request.method == 'POST':
        form=customer_details_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            print('here')
            form.save()
            messages.success(request, f'Customer details for {name} added successfully !!')
            return redirect('customer')
        else:
            messages.error(request, f'The provided customer details with name, number and email already exists !!')
            return redirect('customer')
    else:
        form=customer_details_form()
    context_data=customer_details.objects.all().values()
    context = {
        'form' : form,
        'context_data' : context_data
    }
    return render(request, 'frontend/customer_register.html', context)

# ---------------------------------------------------------------------- end of customer registration view -------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------- start of billing quote view -------------------------------------------------------------------------------------------
@login_required
def billings_process(request):
     if request.method == 'POST':
          form=Generate_bill_quote(request.POST, empty_permitted=False)
          if form and form.is_valid():
               invoice_id=form.cleaned_data['Invoice_number']
               sales_invoice=Sales_Invoice.objects.filter(Invoice_number=invoice_id).values()
               print(sales_invoice)
               return render(request, 'frontend/Invoice_template.html', {'context_dict': sales_invoice})          
     else:
          form=Generate_bill_quote()
          form2=Generate_invoice()
     context_data=Sales_Invoice.objects.filter(Sold_status=False).values()
     context = {
          'context_data' : context_data,
          'form' : form,
          'form2' : form2
     }
     return render(request, 'frontend/Billing_page.html', context)

# ---------------------------------------------------------------------- end of billing quote view -------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------- start of invoice generation view -------------------------------------------------------------------------------------------
@login_required
def generate_Invoice(request):
    if request.method == 'POST':
          form2=Generate_invoice(request.POST)
          if form2.is_valid():
               invoice_id=form2.cleaned_data['Invoice_number']
               payment_id=form2.cleaned_data['Payment_reference_no']
               Sales_Invoice.objects.filter(Invoice_number=invoice_id).update(Payment_reference_no=payment_id, Sold_status=True)
               sales_invoice=Sales_Invoice.objects.filter(Invoice_number=invoice_id).values()
               print(invoice_id, payment_id)
               for items in sales_invoice:
                    if items['Serial_number']:
                        ProductModel.objects.filter(serial_number=items['Serial_number']).update(sales_status=True)
               return render(request, 'frontend/Invoice_template.html', {'context_dict': sales_invoice})               
    else:
          form=Generate_bill_quote()
          form2=Generate_invoice()
    context_data=Sales_Invoice.objects.filter(Sold_status=False).values()
    context = {
          'context_data' : context_data,
          'form' : form,
          'form2' : form2
     }
    return render(request, 'frontend/Billing_page.html', context)

# ---------------------------------------------------------------------- end of invoice generation view -------------------------------------------------------------------------------------------
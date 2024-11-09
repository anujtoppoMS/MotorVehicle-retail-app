from django.shortcuts import render, redirect
from .models import Product, ProductPrice, ProductModel, ProductColour 
from .form import ProductForm, ProductModelForm, ProductColourForm, ProductPriceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import ProductSerializer, ProductModelSerializer, ProductColourSerializer, ProductPriceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@login_required
def update_inventory(request):
    if request.method == 'POST':
        update_stock = ProductForm(request.POST)
        # delete_stock = DeleteProductForm(request.POST)
        print(request.POST)
        if 'update_stock' in request.POST and update_stock.is_valid():
                update_stock.save()
                messages.success(request, f'Product updated successfully')
                return redirect('update_inventory')
        elif 'delete_stock' in request.POST and update_stock.is_valid():
                product_name=update_stock.cleaned_data['name']
                Product.objects.filter(model_type=product_name).update(status=False)
                messages.info(request, f'Product removed successfully {product_name}')
                return redirect('update_inventory')
    else:
        update_stock = ProductForm()
        # delete_stock = DeleteProductForm()
        data_list = Product.objects.filter(status=True).values()
    context={
            'post_data': data_list,
            'update_stock': update_stock,
            }
    return render(request, 'frontend/Update_inventory.html', context)

@login_required
def update_product(request):
        if request.method == 'POST':
        #       product_form = ProductForm(request.POST)
              product_model_form=ProductModelForm(request.POST)
              product_colour_form = ProductColourForm(request.POST)
              product_price_form = ProductPriceForm(request.POST)
              if product_model_form.is_valid() and product_colour_form.is_valid() and product_price_form.is_valid():
                print("--------------here")
                name=product_model_form.cleaned_data['name']

                # Save the product model
                product_model = product_model_form.save()

                # Save the product colour
                product_colour = product_colour_form.save(commit=False)
                product_colour.product_model = product_model
                product_colour.save()

                # Save the product price
                product_price = product_price_form.save(commit=False)
                product_price.product_colour = product_colour
                product_price.save()
                messages.success(request, f'Product Data "{name}" saved successfully')
                return redirect('update_product')
        else:
        #       product_form = ProductForm()
              product_model_form=ProductModelForm()
              product_colour_form = ProductColourForm()
              product_price_form = ProductPriceForm()
        data_list2 = ProductPrice.objects.all()
        list_data=[]
        for first in data_list2:
              list_data.append({'Product':first.product_colour.product_model.product.name, 'Make':first.product_colour.product_model.year_of_make, 'SN':first.product_colour.product_model.serial_number, 
                                'Chassis_No':first.product_colour.product_model.chassis_number, 'Capacity':first.product_colour.product_model.capacity, 'Engine_No':first.product_colour.product_model.engine_number, 
                                'Battery_No':first.product_colour.product_model.battery_number, 'Key_No':first.product_colour.product_model.key_number, 'Colour':first.product_colour.colour_name, 'Price':first.price, 'sales_status' : first.product_colour.product_model.sales_status})
        context = {
        #       'product_form' : product_form,
              'product_model_form' : product_model_form,
              'product_colour_form' : product_colour_form,
              'product_price_form' : product_price_form,
              'data_list' : list_data,
              }
        return render(request, 'frontend/Update_products.html', context)

# @login_required
@api_view(['GET'])       
def getProductData(request):
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)

@login_required
@api_view(['GET'])       
def getProductModelData(request):
      productmodel = ProductModel.objects.all()
      serializer = ProductModelSerializer(productmodel, many=True)
      return Response(serializer.data)

@login_required
@api_view(['GET'])       
def getProductColourData(request):
      productcolour = ProductColour.objects.all()
      serializer = ProductColourSerializer(productcolour, many=True)
      return Response(serializer.data)

@login_required
@api_view(['GET'])       
def getProductPriceData(request):
      productprice = ProductPrice.objects.all()
      serializer = ProductPriceSerializer(productprice, many=True)
      return Response(serializer.data)
      
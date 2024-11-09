from .models import Sales_Invoice, customer_details
from inventory.models import Product, ProductModel, ProductColour, ProductPrice
import requests
import time
import random
import string
# here are the logic to manupulate the DB and filter the output


class filter_output():
    def __init__(self, arg1, arg2, arg3, arg4) -> None:
        self.product_name=arg1
        self.product_colour=arg2
        self.customer_detail=arg3
        self.agent=arg4

    def invoice_gen(self):
        timestamp = int(time.time())
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return f"INV{timestamp}{random_string}"

    def filter_data(self):
        self.product_colour=str(self.product_colour).rsplit('-')
        self.product_colour=self.product_colour[-1].strip()
        self.customer_detail=str(self.customer_detail).split('-')
        self.customer_name=self.customer_detail[0].strip()
        self.customer_number=self.customer_detail[1].strip()
        data_list=[]
        print(self.product_name)
        id=Product.objects.filter(name=self.product_name).values_list('id')
        id = [val for val in id]
        if id:
            product_model=ProductModel.objects.filter(product_id=id[0][0]).values()
            product_colour=ProductColour.objects.filter(id=id[0][0], colour_name=self.product_colour).values()
            product_price=ProductPrice.objects.filter(id=id[0][0]).values()
            customerinfo=customer_details.objects.filter(Name=self.customer_name, Contact=self.customer_number).values()
            if product_model and product_colour and product_price:
                for items in product_model:
                    self.items=items
                for items in product_colour:
                    self.items.update(items)
                for items in product_price:
                    self.items.update(items)
            if customerinfo:
                for item in customerinfo:
                    self.items.update(item)
            temp_name=self.items['name'] 
            temp_yearmake=self.items['year_of_make']
            temp_id=self.items['Identification']

            temp_id_num=self.items['ID_number']
            print('here')
            invoice=Sales_Invoice(Invoice_number=self.invoice_gen(), Make_and_model=f'{temp_name},{temp_yearmake}', 
                                  Serial_number=self.items['serial_number'], Chasis_number=self.items['chassis_number'], Engine_number=self.items['engine_number'],
                                   Battery_number=self.items['battery_number'], Key_number=self.items['key_number'], Customer_name=self.items['Name'], Customer_id=f'{temp_id}, {temp_id_num}', customer_address=self.items['Address'], 
                                    cust_contact=self.items['Contact'], Sales_agent=self.agent, Price_break=self.items['price'])
            invoice.save()

            return self.items
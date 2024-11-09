# n = int(input())
# last_lst=list(input().split())
# result = all([ val==val.strip('-') for val in last_lst])
# if result:
#     result=any([val==val[::-1] for val in last_lst])
#     if result:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# import random
# import string
# import time

# def generate_invoice_number():
#     timestamp = int(time.time())
#     random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#     return f"INV{timestamp}{random_string}"

# invoice_number = generate_invoice_number()
# print(f"Generated Invoice Number: {invoice_number}")


import requests

endpoint = 'http://127.0.0.1:8000/inventory/get_product_colour/'

data = requests.get(endpoint)

print(data.text)
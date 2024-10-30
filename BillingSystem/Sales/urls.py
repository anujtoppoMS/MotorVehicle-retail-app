from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks, name='stocks'),
    path('customer', views.customer_reg, name='customer'),
    path('billings_process', views.billings_process, name='billings_process'),
    path('generate_Invoice', views.generate_Invoice, name='generate_Invoice'),
]
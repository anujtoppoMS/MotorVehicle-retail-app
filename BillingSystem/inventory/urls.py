from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_inventory, name='update_inventory'),
    path('product/', views.update_product, name='update_product'),
    path('get_product/', views.getProductData, name='get_product'),
    path('get_product_model/', views.getProductModelData, name='get_product_model'),
    path('get_product_colour/', views.getProductColourData, name='get_product_colour'),
    path('get_product_price/', views.getProductPriceData, name='get_product_price'),
]
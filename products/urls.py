from django.urls import path

from .views import products_list, add_product, edit_product


urlpatterns = [
    path('products/<pk>', products_list, name='products_list'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/<int:pk>/', edit_product, name='edit_product'),
    

]

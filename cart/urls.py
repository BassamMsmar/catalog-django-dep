from django.urls import path

from .views import cart, add_to_cart, remove_to_cart


urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_to_cart, name='remove_to_cart'),
]

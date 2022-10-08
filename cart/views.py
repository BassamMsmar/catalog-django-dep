from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from products.models import Prducts
from django.db.models import Sum
# Create your views here.


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Prducts, pk=pk)
    cart = Cart.objects.get(user=request.user)

    cart.items.add(product)
    return redirect ('cart')


@login_required
def remove_to_cart(request, pk):
    product = get_object_or_404(Prducts, pk=pk)
    cart = Cart.objects.get(user=request.user)

    cart.items.remove(product)
    return redirect ('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()

    total_price = products.aggregate(Sum('price'))

    return render(request, 'carts/cart.html', {
        'products':products,
        'total_price':total_price,
        })

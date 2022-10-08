from django.shortcuts import redirect, render, get_object_or_404

from .models import Prducts
from .forms import AddProductForm

# Create your views here
def products_list(request, pk):
    # section = Sections.objects.filter(pk=pk)
    product = Prducts.objects.all()
    context ={
        'product':product,
        'pk': int(pk),
        }
    return render(request, 'products/products-list.html', context)


def add_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST,request.FILES)

            if form.is_valid():
                form.save()
                return redirect('sections_list')
        else:
                form = AddProductForm()
    
        context={'form':form}
        return render (request, 'products/add_edit_product.html', context)
    else:
        return redirect('sections_list')


def edit_product(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:

        prducts = get_object_or_404(Prducts, pk=pk)
        if request.method == 'POST':
            form = AddProductForm(request.POST,request.FILES, instance=prducts)

            if form.is_valid():
                form.save()
                return redirect('sections_list')
        else:
                form = AddProductForm(instance=prducts)
    
        context={'form':form}
        return render (request, 'products/add_edit_product.html', context)
    else:
        return redirect('sections_list')
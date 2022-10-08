
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Sections
from .forms import AddFormSection

# Create your views here.

def sections_list(request):
    section = Sections.objects.all()
    context ={
        'section':section
        }
    return render(request, 'sections/sections-list.html', context)


def add_section(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddFormSection(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('sections_list')

        else:
            form = AddFormSection()

        return render(request, 'sections/add_edit_section.html', {'form': form})
    
    else:
        return redirect('sections_list')
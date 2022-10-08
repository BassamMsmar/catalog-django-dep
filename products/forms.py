from django.forms import ModelForm
from .models import Prducts

    

class AddProductForm(ModelForm):
    
    class Meta:
        model = Prducts
        fields = "__all__"

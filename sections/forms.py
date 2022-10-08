from django import forms

from .models import Sections

class AddFormSection(forms.ModelForm):
    class Meta:
        model = Sections
        fields = "__all__"

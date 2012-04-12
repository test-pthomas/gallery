from django import forms
from galleria.models import Gallery

class CreateForm(forms.ModelForm):
    class Meta:
        model = Gallery
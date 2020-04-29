from django.forms import ModelForm
from django import forms
from .models import Man

class MenForm(ModelForm):

    class Meta():
        model = Man
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mx-sm-3'}),
            'email': forms.TextInput(attrs={'class':'form-control mx-sm-3'})
        }

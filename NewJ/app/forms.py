from django.forms import ModelForm
from django import forms
from .models import Man
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

class MenForm(ModelForm):

    class Meta:
        model = Man
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mx-sm-3'}),
            'email': forms.TextInput(attrs={'class':'form-control mx-sm-3'})

        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'a':
            raise ValidationError('Нельзя вводить {}!!'.format(name))
        return name

class LoginFornm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class RegisrerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class']='form-control'


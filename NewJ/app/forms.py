from django.forms import ModelForm
from django import forms
from .models import News, AuthCode, My_User
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField



class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['text', 'author']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'a':
            raise ValidationError('Нельзя вводить {}!!'.format(name))
        return name

class AuthForm(ModelForm):
    class Meta:
        model = AuthCode
        fields = ['auth_code']

class LoginFornm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class RegisrerForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = My_User
        fields = ["username", 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'




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
        fields = ['text', 'author', 'file']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AuthForm(ModelForm):
    class Meta:
        model = AuthCode
        fields = ['auth_code']


class LoginFornm(AuthenticationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = My_User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
        self.fields['password'].help_text = 'ВВедите пароль.'
        self.fields['username'].help_text = 'Введите свой логин.'


class RegisrerForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = My_User
        fields = ["username", 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
        self.fields['email'].help_text = 'Обязательное поле. Введите настоящий адрес электронной почты.'
        self.fields['password1'].help_text = '<ul>' \
                                             '<li>Ваш пароль не может быть слишком похож на другую вашу личную информацию</li>' \
                                             '<li>Ваш пароль должен содержать как минимум 8 символов.</li>' \
                                             '<li>Ваш пароль не может быть часто используемым паролем.</li>' \
                                             '<li>Ваш пароль не должен состоять только из цифр.</li>' \
                                             '</ul>'


class GetFormToken(forms.Form):
    refresh = forms.CharField(label='refresh', max_length=250)
    access = forms.CharField(label='access', max_length=250)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
            self.fields[f].widget.attrs['readonly'] = ''



from allauth.account.forms import SignupForm
from django import forms
from captcha.fields import ReCaptchaField

class MyCustomSignupForm(SignupForm):
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'




from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='')
    password = forms.CharField(widget=forms.PasswordInput, label='')

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(widget=forms.PasswordInput,label='')

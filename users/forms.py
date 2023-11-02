from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


        widgets = {
                'username' : forms.TextInput(attrs={'class': 'form-control'}),
                'email' : forms.TextInput(attrs={'class': 'form-control'}),
                'phone_number' : forms.TextInput(attrs={'class': 'form-control'}),
                'password1' : forms.TextInput(attrs={'class': 'form-control'}),
                'password1' : forms.TextInput(attrs={'class': 'form-control'}),
            }
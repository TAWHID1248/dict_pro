from django import forms
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


        widgets = {
                'title' : forms.TextInput(attrs={'class': 'form-control'}),
                'content' : forms.Textarea(attrs={'class': 'form-control'}),
                'category' : forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            }

from django import forms
from django.forms import fields
from .models import Tag, Category, Post, Comment
from django.contrib.auth import get_user_model, models

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, min_length=3, label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['wirter', 'slug']

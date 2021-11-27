from django import forms
from .models import Tag, Category, Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, min_length=3, label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput)

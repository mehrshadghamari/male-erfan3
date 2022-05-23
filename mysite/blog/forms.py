
from django import forms
from django.forms import ModelForm,Form
from .models import Post


class PostForm (ModelForm):

    class Meta:
        model=Post
        fields='__all__'


class LoginForm(Form):
    username=forms.CharField()
    password=forms.CharField()



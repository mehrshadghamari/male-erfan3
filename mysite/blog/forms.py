from dataclasses import field
from xml.parsers.expat import model
from django.forms import ModelForm
from .models import Post


class PostForm (ModelForm):

    class Meta:
        model=Post
        field='__all__'



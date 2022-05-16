from django.db import models
from django.forms import CharField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time=models.DateTimeField(auto_now=True)
    modified=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.id}-{self.title}'


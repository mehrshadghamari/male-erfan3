from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Post
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from .forms import PostForm

# Create your views here
def index(request):

    return render (request , 'blog/index.html')



def login_user(request):
    pass



def register_user(request):
    pass


def post_list(request):
    posts=Post.objects.all()
    context={'posts':posts}

    return render (request ,'blog/post_list.html' ,context)


def detail_post(request,id):
    
    detail=Post.objects.get(pk=id)
    context={'detail':detail}
    return render (request,'blog/detail_post.html',context)



def add_post(request):

    pass

    


# edit
# get the object
# pass it in template with context
# if object exist it is edit page
# fill the elements with the object value


    


    


from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from .models import Post
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import PostForm,LoginForm



def index(request):

    return render (request , 'blog/index.html')



def login_user(request):

    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd.get('username')
            password=cd.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
            return redirect ('post_list')
        else:
            HttpResponse(' invalid username or password')


    form=LoginForm()
    context={'form':form}
    return render(request,'blog/login_user.html',context)


# def login_user2(request):

#     if request.method=='POST':
#         form=authenticate(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request,user)
#             return redirect ('post_list')

#         else:
#             HttpResponse(' invalid username or password')



#     form=authenticate()
#     context={'form':form}
    # return render(request,'blog/login_user.html',context)



def logout_user(request):
    logout(request)
    return redirect('login_user')
    




def register_user(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            # user=form.save()
            # login(request,user)
            # return redirect('post_list')
            return redirect ('login_user')



    form=UserCreationForm()
    context={'form':form}
    return render(request,'blog/register_user.html',context)


def post_list(request):
    posts=Post.objects.all()
    context={'posts':posts}

    return render (request ,'blog/post_list.html' ,context)


def detail_post(request,id):
    
    detail=Post.objects.get(pk=id)
    context={'detail':detail}
    return render (request,'blog/detail_post.html',context)



def add_post(request):


    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('post_list')


    form=PostForm()
    context={'form':form}
    return render(request,'blog/add_post.html',context)

    
def update_post(request,id):
    post=Post.objects.get(pk=id)
    
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')


    form=PostForm(instance=post)
    context={'form':form}
    return render(request,'blog/update_post.html',context)






    


# edit
# get the object
# pass it in template with context
# if object exist it is edit page
# fill the elements with the object value


    


    


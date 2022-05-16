from operator import index
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('post_list/',views.post_list, name="post_list"),
    path('detail_post/<int:id>',views.detail_post,name="detail_post"),
    path('',views.index),
    path('login_user',views.login_user,name='login'),
    path('register_user',views.register_user,name='register'),

]

from operator import index
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('post_list/',views.post_list, name="post_list"),
    path('detail_post/<int:id>',views.detail_post,name="detail_post"),
    path('add_post/',views.add_post,name='add_post'),
    path('',views.index),
    path('login_user',views.login_user,name='login_user'),
    path('register_user',views.register_user,name='register_user'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('update_post/<int:id>',views.update_post,name='update_post')
]

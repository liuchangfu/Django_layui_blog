# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/27 8:16


from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),
]

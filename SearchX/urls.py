from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'SearchX'



urlpatterns = [
    path('',searchx_main,name='searchx_main'),#搜索主页
    path('searchXresual/',searchXresual,name='searchXresual'),#搜索结果页面

]
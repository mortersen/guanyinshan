from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'DocumentDB'



urlpatterns = [
    path('',documentdb_main,name='documentdb_main'),#文献库主页
    path('periodical/',periodical,name='periodical'),#期刊
    path('periodical/<int:id>/',periodical_detail,name='periodical_detail'),#期刊按ID号显示详细页
    path('dissertation/',dissertation,name='dissertation'),#学位论文,处理翻页
    path('dissertation/<int:id>/',dissertation_detail,name='dissertation_detail'),#学位论文按ID号显示详细页
    path('books/',books,name='books'),#图书
    path('conferencepapers/',conferencepapers,name='conferencepapers'),#会议论文




]
from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'DocumentDB'



urlpatterns = [
    path('',documentdb_main,name='documentdb_main'),#文献库主页
    path('periodical/',periodical,name='periodical'),#期刊
    path('periodical/periodical_by_title/',periodical_by_title,name='periodical_by_title'),#期刊查询结果页
    path('periodical/<int:id>/',periodical_detail,name='periodical_detail'),#期刊按ID号显示详细页
    path('periodical/MC/',periodical_MC,name='periodical_MC'),#期刊二级分类
    path('periodical/MG/',periodical_MG,name='periodical_MG'),#期刊二级分类
    path('periodical/MS/',periodical_MS,name='periodical_MS'),#期刊二级分类
    path('periodical/XQ/',periodical_XQ,name='periodical_XQ'),#期刊二级分类
    path('periodical/YM/',periodical_YM,name='periodical_YM'),#期刊二级分类
    path('periodical/QT/',periodical_QT,name='periodical_QT'),#期刊二级分类
    path('dissertation/',dissertation,name='dissertation'),#学位论文,处理翻页
    path('dissertation/MC/',dissertation_MC,name='dissertation_MC'),#学位论文二级分类
    path('dissertation/MG/',dissertation_MG,name='dissertation_MG'),#学位论文二级分类
    path('dissertation/MS/',dissertation_MS,name='dissertation_MS'),#学位论文二级分类
    path('dissertation/XQ/',dissertation_XQ,name='dissertation_XQ'),#学位论文二级分类
    path('dissertation/YM/',dissertation_YM,name='dissertation_YM'),#学位论文二级分类
    path('dissertation/QT/',dissertation_QT,name='dissertation_QT'),#学位论文二级分类
    path('dissertation/<int:id>/',dissertation_detail,name='dissertation_detail'),#学位论文按ID号显示详细页
    path('dissertation/dissertation_by_title/',dissertation_by_title,name='dissertation_by_title'),#学位论文查询结果页
    path('books/',books,name='books'),#图书
    path('books/<int:id>/',books_detail,name='books_detail'),#图书详细页
    path('books/books_by_title/',books_by_title,name='books_by_title'),#图书查询结果页
    path('conferencepapers/',conferencepapers,name='conferencepapers'),#会议论文
    path('conferencepapers/<int:id>/',conferencepapers_detail,name='conferencepapers_detail'),#会议论文详细页
    path('conferencepapers/conferencepapers_by_title/',conferencepapers_by_title,name='conferencepapers_by_title'),#会议论文查询结果页
]
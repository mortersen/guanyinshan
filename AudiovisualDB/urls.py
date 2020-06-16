from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'AudiovisualDB'


urlpatterns = [
    path('',audiovisualdb_main,name='audiovisualdb_main'),#口述史料库主页
    #path('operatext/',operatext,name='operatext'),#戏曲文本
    #path('operatext/<int:id>/',operatext_detail,name='operatext_detail'),#戏曲文本按ID号显示详细页
    #path('folksong/',folksong,name='folksong'),#歌谣,处理翻页
    #path('folksong/<int:id>/',folksong_detail,name='folksong_detail'),#歌谣按ID号显示详细页

]
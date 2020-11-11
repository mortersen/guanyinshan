from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'AudiovisualDB'


urlpatterns = [
    path('',audiovisualdb_main,name='audiovisualdb_main'),#口述史料库主页
    path('video/',video,name='video'),#戏曲文本
    path('video/XQ/',video_XQ,name='video_XQ'),#视频二级分类
    path('video/TY/',video_TY,name='video_TY'),#视频二级分类
    path('video/SJ/',video_SJ,name='video_SJ'),#视频二级分类
    path('video/SG/',video_SG,name='video_SG'),#视频二级分类
    path('video/CT/',video_CT,name='video_CT'),#视频二级分类
    #path('operatext/<int:id>/',operatext_detail,name='operatext_detail'),#戏曲文本按ID号显示详细页
    path('audio/',audio,name='audio'),#歌谣,处理翻页
    path('audio/GY/',audio_GY,name='audio_GY'),#音频二级分类
    path('audio/GS/',audio_GS,name='audio_GS'),#音频二级分类
    path('audio/KL/',audio_KL,name='audio_KL'),#音频二级分类
    #path('folksong/<int:id>/',folksong_detail,name='folksong_detail'),#歌谣按ID号显示详细页

]
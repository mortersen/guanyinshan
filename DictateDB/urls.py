from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'DictateDB'


urlpatterns = [
    path('',dictatedb_main,name='dictatedb_main'),#口述史料库主页
    path('operatext/',operatext,name='operatext'),#戏曲文本
    path('operatext/<int:id>/',operatext_detail,name='operatext_detail'),#戏曲文本按ID号显示详细页
    path('operatext/operatext_by_title/',operatext_by_title,name='operatext_by_title'),#戏曲文本查询结果页
    path('folksong/',folksong,name='folksong'),#歌谣,处理翻页
    path('folksong/<int:id>/',folksong_detail,name='folksong_detail'),#歌谣按ID号显示详细页
    path('folksong/folksong_by_title/',folksong_by_title,name='folksong_by_title'),#歌谣查询结果页
    path('songbook/',songbook,name='songbook'),#歌册
    path('songbook/<int:id>/',songbook_detail,name='songbook_detail'),#歌册详细页按ID显示
    path('songbook/songbook_by_title/',songbook_by_title,name='songbook_by_title'),#歌册查询结果页
    path('southernmusic/',southernmusic,name='southernmusic'),#南音曲谱
    path('southernmusic/<int:id>/',southernmusic_detail,name='southernmusic_detail'),#南音曲谱按ID详细页
    path('southernmusic/southernmusic_by_title/',southernmusic_by_title,name='southernmusic_by_title'),#南音曲谱查询结果页
]
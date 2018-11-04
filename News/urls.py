from django.urls import path
from .views import *


app_name = 'News'


urlpatterns = [
    path('',news_top_list,name='news_top_list'),
    path('<int:id>/',news_detail_byid,name='news_detail'),
]
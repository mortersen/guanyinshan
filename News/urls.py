from django.urls import path
from .views import *


app_name = 'News'


urlpatterns = [
    path('page/',news_top_list,name='news_top'),
    path('page/<int:page_index>/',news_top_list,name='news_page'),
    path('<int:id>/',news_detail_byid,name='news_detail'),
]
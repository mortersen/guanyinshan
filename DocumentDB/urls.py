from django.urls import path
from django.shortcuts import render
from .views import *

app_name = 'DocumentDB'


def documentdb_base(request):
    return render(request,'documentdb_base.html')


urlpatterns = [
    path('',documentdb_base,name='document_db_main'),
    path('periodical/',periodical_main,name='periodical_main'),
    path('periodical/page/<int:page_num>',periodical_page,name='periodical_page'),


]
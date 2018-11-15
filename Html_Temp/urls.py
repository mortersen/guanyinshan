"""Html_Temp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.shortcuts import render,redirect,reverse

from django.conf import settings #引入MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static#引入static方法将网址解析转成本地路径解析


def index(request):
    return render(request,'index.html')
'''

def turntoindex(request):
    temp_url = reverse('index')
    print(temp_url, request)
    return redirect(temp_url)
'''

def test(request):
    return render(request,'test.html')

def managepage(request):
    return redirect('../admin/')

urlpatterns = [
    path('',index),
    path('index/',index,name='index'),
    path('test/',test,name="test"),
    path('news/',include('News.urls',namespace='News')),
    path('documentdb/',include('DocumentDB.urls',namespace="DocumentDB")),
    path('admin/', admin.site.urls),
    path('gly/',managepage,name='managepage'),
    #re_path(r'',turntoindex),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#用于将media路径解析到本地media
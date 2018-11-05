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
from django.views.static import serve #处理MEDIA_URL 路由
from Html_Temp.settings import MEDIA_ROOT


def index(request):
    return render(request,'index.html')


def turntoindex(request):
    temp_url = reverse('index')
    print(temp_url, request)
    return redirect(temp_url)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('news/',include('News.urls',namespace='News')),
    path('media/(?p<path>.*)',serve,{"document_root":MEDIA_ROOT}),#处理MEDIA路由
    re_path(r'',turntoindex),
]

from django.shortcuts import render
from .models import Information
from django.http import Http404
# Create your views here.


def news_top_list(request):
    info = Information.objects.all()
    content = {'info' : info}
    return render(request, 'news_top_list.html',content)


def news_detail_byid(request,id):
    try:
        news_item = Information.objects.get(id = id)
        content = {'news_item' : news_item}
    except:
        return Http404
    return render(request, 'news_detail_byid', content)

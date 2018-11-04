from django.shortcuts import render,HttpResponse
from .models import Information
from django.http import Http404
# Create your views here.


def news_top_list(request):
    info = Information.objects.all()
    content = {'info' : info}
    return render(request, 'news_top_list.html',content)


def news_detail_byid(request,id):
    try:
        info = Information.objects.get(id = id)
    except Exception as err:
        return Http404(str(err))
    #以上内容需完善
    return render(request,"news_detail_byid.html",{'info':info})


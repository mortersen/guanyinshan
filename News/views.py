from django.shortcuts import render,HttpResponse
from .models import Information,R_Information_Photo
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger#引入分页模块和类

# Create your views here.


def news_top_list(request,num = 1):
    all_info = Information.objects.all().order_by("-updatetime")
    pages = Paginator(all_info,5)#按5为单位将news对象分割成分页对象组
    info = pages.page(num)#取第num页对象列表
    content = {'info' : info,'pages':pages}
    return render(request, 'news_top_list.html',content)


def news_detail_byid(request,id):
    try:
        info = Information.objects.get(id = id)
        pic = R_Information_Photo.objects.filter(information_id=id).first()

    except Exception as err:
        raise Http404('NOT FOUND ID: ' + str(err))

    #以上内容需完善
    return render(request,"news_detail_byid.html",{'info':info,'pic':pic})


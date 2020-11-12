from django.shortcuts import render,HttpResponse
from .models import Information,R_Information_Photo
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger#引入分页模块和类

# Create your views here.


def news_top_list(request):
    list = Information.objects.all().order_by("-updatetime")
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 5)
    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)
    # print(cur_dissertation.paginator.count)
    # print(cur_dissertation.number)
    return render(request,'news_top_list.html', {'cur_dissertation': cur_dissertation})

def news_detail_byid(request,id):
    try:
        info = Information.objects.get(id = id)
        pic = R_Information_Photo.objects.filter(information_id=id).first()

    except Exception as err:
        raise Http404('NOT FOUND ID: ' + str(err))

    #以上内容需完善
    return render(request,"news_detail_byid.html",{'info':info,'pic':pic})


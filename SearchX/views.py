from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from DocumentDB.models import Books,Periodical,Dissertation,ConferencePapers
from DictateDB.models import OperaText,FolkSong,SongBook,SouthernMusic
from AudiovisualDB.models import Audio,Video
from DocumentDB.views import books_by_title,periodical_by_title,dissertation_by_title,conferencepapers_by_title
from DictateDB.views import operatext_by_title,folksong_by_title,songbook_by_title,southernmusic_by_title
# Create your views here.

def searchx_main(request):

    target = {'':'',}
    return render(request, 'searchx/searchx.html', target)

def searchXresual(request):
    if request.method == 'POST':
        sdb = request.POST.get("sdb")
        skey = request.POST.get("skey").replace(' ','').replace(' ','')
    if skey == '':
        return render(request,'searchx/searchx.html',)
    print(sdb, skey)

    if sdb == 'TS':
        return books_by_title(request,skey)
    elif sdb == 'QK':
        return periodical_by_title(request,skey)
    elif sdb == 'XWLW':
        return dissertation_by_title(request,skey)
    elif sdb == 'HYLW':
        return conferencepapers_by_title(request,skey)
    elif sdb == 'XQWB':
        return operatext_by_title(request,skey)
    elif sdb == 'GY':
        return folksong_by_title(request,skey)
    elif sdb == 'GC':
        return songbook_by_title(request,skey)
    elif sdb == 'NYQP':
        return southernmusic_by_title(request,skey)
    if searchlist.count() == 0:
        return HttpResponse("查询结果为空！")

    paginator = Paginator(searchlist, 8)
    page = request.GET.get('page')
    print(page)
    try:
        target = paginator.page(page)

    except PageNotAnInteger:
        target = paginator.page(1)
    except EmptyPage:
        target = paginator.page(paginator.num_pages)

    for item in target:
        print(item.Title)

    return render(request,'searchx/searchlist.html',{'cur_dissertation':target,'sourcepath':sourcepath})
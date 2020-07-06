from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from DocumentDB.models import Books,Periodical,Dissertation,ConferencePapers
from DictateDB.models import OperaText,FolkSong,SongBook,SouthernMusic
from AudiovisualDB.models import Audio,Video
from DocumentDB.views import books_by_title

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
        searchlist = Periodical.objects.filter(Title__contains=skey)
        sourcepath = 'DocumentDB:periodical_detail'
    elif sdb == 'XWLW':
        searchlist = Dissertation.objects.filter(Title__contains=skey)
        sourcepath = 'DocumentDB:dissertation_detail'
    elif sdb == 'HYLW':
        searchlist = ConferencePapers.objects.filter(Title__contains=skey)
        sourcepath = 'DocumentDB:conferencepapers_detail'
    elif sdb == 'XQWB':
        searchlist = OperaText.objects.filter(Title__contains=skey)
        sourcepath = 'DictateDB:operatext_detail'
    elif sdb == 'GY':
        searchlist = FolkSong.objects.filter(Title__contains=skey)
        sourcepath = 'DictateDB:folksong_detail'
    elif sdb == 'GC':
        searchlist = SongBook.objects.filter(Title__contains=skey)
        sourcepath = 'DictateDB:songbook_detail'
    elif sdb == 'NYQP':
        searchlist = SouthernMusic.objects.filter(Title__contains=skey)
        sourcepath = 'DictateDB:southernmusic_detail'
    elif sdb == 'SP':
        searchlist = Video.objects.filter(Title__contains=skey)
        sourcepath = 'AudiovisualDB:video'
    elif sdb == 'YP':
        searchlist = Audio.objects.filter(Title__contains=skey)
        sourcepath = 'AudiovisualDB:audio'

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
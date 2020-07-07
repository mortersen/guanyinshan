from django.shortcuts import render,Http404,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import OperaText,FolkSong,SongBook,SouthernMusic

# Create your views here.

def dictatedb_main(request):
    operatext_count = OperaText.objects.count()
    folksong_count = FolkSong.objects.count()
    songbook_count = SongBook.objects.count()
    #print(songbook_count)
    southernmusic_count = SouthernMusic.objects.count()
    dictatedb_count = operatext_count + folksong_count + songbook_count + southernmusic_count

    target = {'operatext_count':operatext_count,'folksong_count':folksong_count,\
                'songbook_count':songbook_count,'southernmusic_count':southernmusic_count,\
              'dictatedb_count':dictatedb_count
                }
    #print(target)
    return render(request,'dictatedb/dictatedb_main.html',target)



def operatext(request):
    list = OperaText.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    return render(request,'dictatedb/operatext.html',{'cur_dissertation':cur_dissertation,})



def operatext_detail(request,id):
    target = OperaText.objects.get(id=id)
    return render(request,'dictatedb/operatext_detail.html',{'target':target})


def operatext_by_title(request,str=''):
    if str== '':
        str = request.GET.get('skey')
    bylist = OperaText.objects.filter(Title__contains=str)
    count = bylist.count()
    if count == 0:
        return HttpResponse("查询结果为空！")
    else:
        page = request.GET.get('page')
        paginator = Paginator(bylist, 6)

        try:
            cur_dissertation = paginator.page(page)

        except PageNotAnInteger:
            cur_dissertation = paginator.page(1)
        except EmptyPage:
            cur_dissertation = paginator.page(paginator.num_pages)
        # print(cur_dissertation.paginator.count)
        # print(cur_dissertation.number)
        return render(request, 'DictateDB/operatext_by_title.html', {'cur_dissertation': cur_dissertation,'skey':str,'count':count,})


def folksong(request):
    list = FolkSong.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    return render(request, 'dictatedb/folksong.html', {'cur_dissertation': cur_dissertation, })


def folksong_detail(request,id):
    target = FolkSong.objects.get(id=id)
    return render(request, 'dictatedb/folksong_detail.html', {'target': target})

def folksong_by_title(request,str=''):
    if str== '':
        str = request.GET.get('skey')
    bylist = FolkSong.objects.filter(Title__contains=str)
    count = bylist.count()
    if count == 0:
        return HttpResponse("查询结果为空！")
    else:
        page = request.GET.get('page')
        paginator = Paginator(bylist, 6)

        try:
            cur_dissertation = paginator.page(page)

        except PageNotAnInteger:
            cur_dissertation = paginator.page(1)
        except EmptyPage:
            cur_dissertation = paginator.page(paginator.num_pages)
        # print(cur_dissertation.paginator.count)
        # print(cur_dissertation.number)
        return render(request, 'DictateDB/folksong_by_title.html', {'cur_dissertation': cur_dissertation,'skey':str,'count':count,})


def songbook(request):
    list = SongBook.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    return render(request, 'dictatedb/songbook.html', {'cur_dissertation': cur_dissertation, })


def songbook_detail(request,id):
    target = SongBook.objects.get(id=id)
    return render(request, 'dictatedb/songbook_detail.html', {'target': target})


def songbook_by_title(request,str=''):
    if str== '':
        str = request.GET.get('skey')
    bylist = SongBook.objects.filter(Title__contains=str)
    count = bylist.count()
    if count == 0:
        return HttpResponse("查询结果为空！")
    else:
        page = request.GET.get('page')
        paginator = Paginator(bylist, 6)

        try:
            cur_dissertation = paginator.page(page)

        except PageNotAnInteger:
            cur_dissertation = paginator.page(1)
        except EmptyPage:
            cur_dissertation = paginator.page(paginator.num_pages)
        # print(cur_dissertation.paginator.count)
        # print(cur_dissertation.number)
        return render(request, 'DictateDB/songbook_by_title.html', {'cur_dissertation': cur_dissertation,'skey':str,'count':count,})


def southernmusic(request):
    list = SouthernMusic.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    return render(request, 'dictatedb/southernmusic.html', {'cur_dissertation': cur_dissertation, })



def southernmusic_detail(request,id):
    target = SouthernMusic.objects.get(id=id)
    return render(request, 'dictatedb/southernmusic_detail.html', {'target': target})


def southernmusic_by_title(request,str=''):
    if str== '':
        str = request.GET.get('skey')
    bylist = SouthernMusic.objects.filter(Title__contains=str)
    count = bylist.count()
    if count == 0:
        return HttpResponse("查询结果为空！")
    else:
        page = request.GET.get('page')
        paginator = Paginator(bylist, 6)

        try:
            cur_dissertation = paginator.page(page)

        except PageNotAnInteger:
            cur_dissertation = paginator.page(1)
        except EmptyPage:
            cur_dissertation = paginator.page(paginator.num_pages)
        # print(cur_dissertation.paginator.count)
        # print(cur_dissertation.number)
        return render(request, 'DictateDB/southernmusic_by_title.html', {'cur_dissertation': cur_dissertation,'skey':str,'count':count,})

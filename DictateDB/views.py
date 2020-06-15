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



def songbook(request):


    return render(request,dictatedb/songbook.html,{})



def songbook_detail(request,id):


    return render(request,dictatedb/songbook_detail.html,{})


def southernmusic(request):


    return render(request,dictatedb/southernmusic.html,{})



def southernmusic_detail(request,id):


    return render(request,dictatedb/southernmusic_detail.html,{})
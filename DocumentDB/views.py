from django.shortcuts import render,Http404,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Periodical,Dissertation


# Create your views here.
def documentdb_main(request):
    return render(request,'documentdb/documentdb_main.html')


def songbook(request):
    return HttpResponse('Building')


def operatext(request):
    return HttpResponse('Building')


def nanyinopern(request):
    return HttpResponse('南音曲谱 Building')


def periodical(request):


    return render(request,'documentdb/periodical.html')


def dissertation(request):
    list = Dissertation.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(list,10)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    #print(cur_dissertation.paginator.count)
    #print(cur_dissertation.number)
    return render(request,'documentdb/dissertation.html',{'cur_dissertation':cur_dissertation})


def dissertation_detail(request,id):
    target = Dissertation.objects.get(id = id)
    return render(request,'documentdb/dissertation_detail.html',{'target':target})


def books(request):
    return HttpResponse('Building')


def newspaper(request):
    return HttpResponse('Building')


def periodical_main(request):

    try:
        items = Periodical.objects.all()
        #print(items.count())
        pages = Paginator(items,8)
        page = pages.page(1)
        content = {'page':page,'page_num':1,'num_pages':pages.num_pages}
    except Exception as err:
        raise Http404('NOT FOUND ID: ' + str(err))

    return render(request,'periodical_main.html',content)



def periodical_page(request,page_num=1):

    try:
        items = Periodical.objects.all()
        #print(items.count())
        pages = Paginator(items,8)
        page = pages.page(page_num)
        content = {'page':page,'page_num':page_num,'num_pages':pages.num_pages}
    except Exception as err:
        raise Http404('NOT FOUND ID: ' + str(err))

    return render(request,'periodical_main.html',content)
from django.shortcuts import render,Http404,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Periodical,Dissertation,Books,ConferencePapers


# Create your views here.
def documentdb_main(request):
    #查询数据统计各种文献资源数量后传输进入
    periodical_count = Periodical.objects.count()
    #print(periodical_count)
    dissertation_count = Dissertation.objects.count()
   # print(dissertation_count)
    conferencepapers_count = ConferencePapers.objects.count()
    #print(conferencepapers_count)
    books_count = Books.objects.count()
    #print(books_count)

    documentdb_count = periodical_count + dissertation_count + conferencepapers_count + books_count
   # print(documentdb_count)

    target = {
            'periodical_count': periodical_count, 'dissertation_count': dissertation_count, \
                   'conferencepapers_count': conferencepapers_count, 'books_count': books_count, \
                   'documentdb_count': documentdb_count
            }

    return render(request,'documentdb/documentdb_main.html',target)


def periodical(request):
    list = Periodical.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    # print(cur_dissertation.paginator.count)
    # print(cur_dissertation.number)
    return render(request, 'documentdb/periodical.html', {'cur_dissertation': cur_dissertation})



def periodical_detail(request,id):
    target = Periodical.objects.get(id=id)
    return render(request, 'documentdb/periodical_detail.html', {'target': target})



def dissertation(request):
    list = Dissertation.objects.all()
    page = request.GET.get('page')
    #print(page)
    paginator = Paginator(list,8)

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
    list = Books.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)
    # print(cur_dissertation.paginator.count)
    # print(cur_dissertation.number)
    return render(request, 'documentdb/books.html', {'cur_dissertation': cur_dissertation})

def books_detail(request,id):
    target = Books.objects.get(id = id)
    return render(request,'documentdb/books_detail.html',{'target':target})


def conferencepapers(request):
    list = ConferencePapers.objects.all()
    page = request.GET.get('page')
    # print(page)
    paginator = Paginator(list, 8)

    try:
        cur_dissertation = paginator.page(page)

    except PageNotAnInteger:
        cur_dissertation = paginator.page(1)
    except EmptyPage:
        cur_dissertation = paginator.page(paginator.num_pages)

    # print(cur_dissertation.paginator.count)
    # print(cur_dissertation.number)
    return render(request, 'documentdb/conferencepapers.html', {'cur_dissertation': cur_dissertation})

def conferencepapers_detail(request,id):
    target = ConferencePapers.objects.get(id = id)
    return render(request,'documentdb/conferencepapers_detail.html',{'target':target})


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



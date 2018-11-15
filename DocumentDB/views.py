from django.shortcuts import render,Http404
from django.core.paginator import Paginator
from .models import Periodical


# Create your views here.

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
from django.shortcuts import render

# Create your views here.

def searchx_main(request):

    target = {'':'',}
    return render(request, 'searchx/searchx.html', target)
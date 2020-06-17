from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
from .models import  Video,Audio

def audiovisualdb_main(request):
    video_count = Video.objects.count()
    audio_count = Audio.objects.count()
    audiovisualdb_count = video_count + audio_count
    print(audiovisualdb_count)
    target = {'video_count':video_count,'audio_count':audio_count,'audiovisualdb_count':audiovisualdb_count}
    return render(request,'audiovisualdb/audiovisualdb_main.html',target)


def video(request):
    list = Video.objects.all()
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


    return render(request,'audiovisualdb/video.html',{'cur_dissertation':cur_dissertation,})



def audio(request):
    list = Video.objects.all()
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

    return render(request,'audiovisualdb/audio.html',{'cur_dissertation':cur_dissertation,})
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




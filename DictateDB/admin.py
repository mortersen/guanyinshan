from django.contrib import admin
from .models import OperaText,SongBook,FolkSong,SouthernMusic
# Register your models here.

admin.site.register(OperaText)
admin.site.register(SongBook)
admin.site.register(FolkSong)
admin.site.register(SouthernMusic)

from django.contrib import admin
from .models import Periodical,Newspaper,Dissertation,Books,OtherDocument
# Register your models here.

admin.site.register(Periodical)
admin.site.register(Newspaper)
admin.site.register(Dissertation)
admin.site.register(Books)
admin.site.register(OtherDocument)

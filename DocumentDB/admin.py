from django.contrib import admin
from .models import Periodical,Dissertation,Books,ConferencePapers
# Register your models here.

admin.site.register(Periodical)
admin.site.register(Dissertation)
admin.site.register(Books)
admin.site.register(ConferencePapers)

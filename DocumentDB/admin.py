from django.contrib import admin
from .models import Periodical,Dissertation,Books,ConferencePapers
# Register your models here.

admin.site.register(Periodical)
admin.site.register(Dissertation)
admin.site.register(Books)
admin.site.register(ConferencePapers)

#修改DJANGO后台界面所有的标题，只需在任意一处admin.py中添加一下一行代码
admin.site.site_header = '闽南口头传承非物质文化遗产数据库'

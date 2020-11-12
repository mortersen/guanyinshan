from django.shortcuts import render
from .models import Consult
# Create your views here.

def consult_main(request ):
    ctx = {}
    if request.method == 'POST':
        title = request.POST.get("title")
        context = request.POST.get("context")
        contact = request.POST.get("contact")
        print(title,context,contact)
        if title == "":
            ctx['rlt'] = "标题不能为空！"
        elif context == "":
            ctx['rlt'] = "内容不能为空！"
        elif contact == "":
            ctx['rlt'] = "请留下联系方式！"
        else:
            ctx['rlt'] = "咨询内容已提交！"

    return render(request,'OnlineConsult/consult.html',ctx)

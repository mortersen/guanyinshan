from django.shortcuts import render
from .models import Consult
# Create your views here.

def consult_main(request ):
    ctx = {}
    if request.method == 'POST':
        title = request.POST.get("title").strip()
        context = request.POST.get("context").strip()
        contact = request.POST.get("contact").strip()
        print(title,context,contact)
        if title == "":
            ctx['rlt'] = "标题不能为空！"
        elif context == "":
            ctx['rlt'] = "内容不能为空！"
        elif contact == "":
            ctx['rlt'] = "请留下联系方式！"
        else:
            data = Consult(Title=title,Context=context,Contact=contact)
            data.save()
            ctx['rlt'] = "咨询内容已提交！"

    return render(request,'OnlineConsult/consult.html',ctx)

import json

from django.http import HttpResponse
from django.shortcuts import render
from users.models import User


def Recent_chat(request):
    # user=User.objects.get(loginid=request.COOKIES.get('LoginID'))
    # return render(request, "Home/Recent_chat.html",{"user":user})
    return render(request, "Home/Recent_chat.html")

def Friends_list(request):
    return render(request, "Home/Friends_list.html")

def Find_Friends(request):
    return render(request, "Home/Find_Friends.html")

def getHeadPortrait(request):
    user = User.objects.get(loginid=request.COOKIES.get('LoginID'))
    return HttpResponse(json.dumps(
        {"headportrait":"/static/HeadPortrait/"+user.headportrait}
    ))

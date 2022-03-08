import json

from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from users.models import User
from . import HomeController


def Recent_chat(request):
    if request.user.is_superuser:
        logout(request)
        return HttpResponseRedirect('/Login')
    ID=request.COOKIES.get('LoginID')
    user=User.objects.get(loginid=ID)
    return render(request, "Home/Recent_chat.html",{"user":HomeController.get_myInfo(user),
                                                    "friends":HomeController.getFriends(ID),
                                                    "friendGroup": HomeController.getFriendGroup(ID),
                                                    "OneWord":HomeController.getOneWord(),
                                                    "Recentmessage":HomeController.getRecentmessage(ID)})

def Friends_list(request):
    return render(request, "Home/Friends_list.html")

def Find_Friends(request):
    return render(request, "Home/Find_Friends.html")

def Chat_panel(request):
    return render(request, "Home/Chat_panel.html")

def EditSign(request):
    if(HomeController.EditSign(request)):
        status = 1
    else:
        status = 0
    return HttpResponse(json.dumps({
        "status": status}))

def EditUserName(request):
    if(HomeController.EditUserName(request)):
        status = 1
    else:
        status = 0
    return HttpResponse(json.dumps({
        "status": status}))

def getFriendInfo(request):
    return HttpResponse(HomeController.getFriendInfo(request))

def getChatInfo(request):
    return HttpResponse(HomeController.getChatInfo(request))
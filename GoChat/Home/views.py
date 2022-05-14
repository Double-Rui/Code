import json
import os
import django
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from users.models import User
from . import HomeController
from .cache_manager import get_Messages_record


def Recent_chat(request):
    if request.user.is_superuser:
        logout(request)
        return HttpResponseRedirect('/Login')
    ID=request.COOKIES.get('LoginID')
    user=User.objects.get(loginid=ID)
    return render(request, "Home/Recent_chat.html", {"user":HomeController.get_myInfo(user),
                                                    "friends":HomeController.getFriends(ID),
                                                    "friendGroup": HomeController.getFriendGroup(ID),
                                                    "OneWord":HomeController.getOneWord(),
                                                    "Recentmessage":HomeController.getRecentmessage(request),
                                                    "Groups":HomeController.getGroups(ID),
                                                    "FriendGroups":HomeController.getFriendGroups(request)})

# def Friends_list(request):
#     return render(request, "Home/Friends_list.html")
#
# def Find_Friends(request):
#     return render(request, "Home/Find_Friends.html")
#
# def Chat_panel(request):
#     return render(request, "Home/Chat_panel.html")

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

def getGroupInfo(request):
    return HttpResponse(HomeController.getGroupInfo(request))

def RefreshRecentmessage(request):
    return HttpResponse(json.dumps(HomeController.RefreshRecentmessage(request)))

def ToChat(request):
    if request.method == "POST":
        Objectid = request.POST.get("objectid")
        UserID = request.COOKIES.get('LoginID')
        Messagestype = request.POST.get("messagestype")
        return HttpResponse(json.dumps({"Messages_record":get_Messages_record(UserID,Objectid,Messagestype),
                             "ChatInfo":HomeController.getChatInfo(request)}))
    else:
        pass

def EditUserInfo(request):
    if request.method == "POST":
        if (HomeController.EditUserInfo(request)):
            status = 1
        else:
            status = 0
        return HttpResponse(json.dumps({
            "status": status}))
    else:
        pass

def Find_friends(request):
    if request.method == "POST":
        Str = request.POST.get("str")
        if(Str=="" or Str==None):
            return HttpResponse({'status':0,'result':'未搜索到相关结果'})
        return HttpResponse(json.dumps(HomeController.Find_friends(Str)))
    else:
        pass

def Find_groups(request):
    if request.method == "POST":
        Str = request.POST.get("str")
        if(Str=="" or Str==None):
            return HttpResponse({'status':0,'result':'未搜索到相关结果'})
        return HttpResponse(json.dumps(HomeController.Find_groups(Str)))
    else:
        pass

def EditAvatar(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditAvatar(request)))
    else:
        pass

def getFriendGroups(request):
    if request.method == "GET":
        return HttpResponse(json.dumps(HomeController.getFriendGroups(request)))
    else:
        pass

def getAddFriend_applylist(request):
    if request.method == "GET":
        return HttpResponse(json.dumps(HomeController.getAddFriend_applylist(request)))
    else:
        pass

def getAddGroup_applylist(request):
    if request.method == "GET":
        return HttpResponse(json.dumps(HomeController.getAddGroup_applylist(request)))
    else:
        pass

def verificat_isfriend(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result':HomeController.verificat_isfriend(request)}))
    else:
        pass

def Processing_requests(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.Processing_requests(request)))
    else:
        pass

def ChangePassword(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.ChangePassword(request)))
    else:
        pass

def NewSession(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.NewSession(request)))
    else:
        pass

def DeleteSession(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.DeleteSession(request)))
    else:
        pass

def DeleteFriend(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.DeleteFriend(request)))
    else:
        pass

def EditFriendname(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditFriendname(request)))
    else:
        pass

def EditGroupname(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditGroupname(request)))
    else:
        pass

def EditGroupUserremarks(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditGroupUserremarks(request)))
    else:
        pass

def EditFriendGroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditFriendGroup(request)))
    else:
        pass

def getFriendGroup(request):
    if request.method == "GET":
        ID = request.COOKIES.get('LoginID')
        return HttpResponse(json.dumps(HomeController.getFriendGroup(ID)))
    else:
        pass

def getGroupslist(request):
    if request.method == "GET":
        ID = request.COOKIES.get('LoginID')
        return HttpResponse(json.dumps(HomeController.getGroupslist(ID)))
    else:
        pass

def MoveFriendGroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.MoveFriendGroup(request)))
    else:
        pass

def AddFriendGroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.AddFriendGroup(request)))
    else:
        pass

def DeleteFriendGroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.DeleteFriendGroup(request)))
    else:
        pass

def EditFriendGroupname(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditFriendGroupname(request)))
    else:
        pass

def EditHeaderstyle(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditHeaderstyle(request)))
    else:
        pass

def Editgroupverification(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.Editgroupverification(request)))
    else:
        pass

def Disbandgroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.Disbandgroup(request)))
    else:
        pass

def Exitgroup(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.Exitgroup(request)))
    else:
        pass

def SetupAdmin(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.SetupAdmin(request)))
    else:
        pass

def RemoveMembers(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.RemoveMembers(request)))
    else:
        pass

def EditProfile(request):
    if request.method == "POST":
        return HttpResponse(json.dumps(HomeController.EditProfile(request)))
    else:
        pass
import json
import requests
from users.models import User,UserInfo
from Home.models import Friends,FriendsGroup
from django.forms.models import model_to_dict


def EditSign(request):
    if request.method == "POST":
        NewSign=request.POST.get("NewSign")
        user = User.objects.get(loginid=request.COOKIES.get('LoginID'))
        user.sign=NewSign
        user.save()
        if(user != None):
            return True
        else:
            return False

def getFriendGroup(ID):

    friendsgroup = FriendsGroup.objects.filter(userid=ID)
    result=[]
    for i in friendsgroup:
        friends = Friends.objects.filter(userid=ID,friendgroupsid=i.groupid)
        children=[]
        for j in friends:
            children.append({
                "username":User.objects.get(loginid=j.friendid).username,
                "headportrait":User.objects.get(loginid=j.friendid).headportrait,
                "sign":str(User.objects.get(loginid=j.friendid).sign)
            })
        result.append({
            "groupname": i.groupname,
            "serialnumber": i.serialnumber,
            "children": children
        })
    return result

def getFriends(ID):
    friends = Friends.objects.filter(userid=ID)
    # friends=model_to_dict(friends)
    result={}
    j=0
    for i in friends:
        result[j]=model_to_dict(i)
        j+=1
    return result

def get_myInfo(user):
    UserInfo.id = user.loginid
    UserInfo.username = user.username
    UserInfo.sex = user.sex
    UserInfo.age = user.age
    UserInfo.headportrait = user.headportrait
    UserInfo.phonenumber = user.phonenumber
    UserInfo.address = user.address
    UserInfo.bloodtype = user.bloodtype
    UserInfo.datebirth = user.datebirth
    UserInfo.constellation = user.constellation
    UserInfo.mail = user.mail
    UserInfo.shengxiao = user.shengxiao
    UserInfo.sign = user.sign
    UserInfo.profession = user.profession
    UserInfo.region = user.region
    return UserInfo

def getOneWord():
    url = 'https://v1.hitokoto.cn/'
    wb_data = requests.get(url)
    data = wb_data.json()
    if data != None:
        hitokoto = data['hitokoto']+"——"+data['from']
        return hitokoto
    else:
        return "也无风雨也无晴"

def EditUserName(request):
    if request.method == "POST":
        NewUserName=request.POST.get("NewUserName")
        user = User.objects.get(loginid=request.COOKIES.get('LoginID'))
        user.username=NewUserName
        user.save()
        if(user != None):
            return True
        else:
            return False
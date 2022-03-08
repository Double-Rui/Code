import json
import requests
from users.models import User,UserInfo
from Home.models import Friends,FriendsGroup,Messageslist
from django.forms.models import model_to_dict
from Home import jiami
import base64
from urllib import parse

key='19991229'


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
            friend=User.objects.get(loginid=j.friendid)
            children.append({
                # "id":jiami.des_encrypt(key,str(friend.loginid)),
                "id":friend.loginid,
                "username":friend.username,
                "headportrait":friend.headportrait,
                "sign":str(isNull(friend.sign))
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
    try:
        wb_data = requests.get(url)
        data = wb_data.json()
        if data != None:
            hitokoto = data['hitokoto'] + "——" + data['from']
            return hitokoto
        else:
            return "也无风雨也无晴"
    except requests.exceptions.ConnectionError:
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

def isNull(value):
    if value:
        return value
    else:
        return ""

def getFriendInfo(request):
    if request.method == "POST":
        friendid = request.POST.get("friendid")
        user = User.objects.get(loginid=int(friendid))
        if user:
            result =json.dumps({
            "username" : user.username,
            "headportrait" : user.headportrait,
            "Info" : [{"labelname":'账号',"content" : str(isNull(user.loginid))},
                    {"labelname": '性别', "content" : str(isNull(user.sex))},
                    {"labelname": '年龄', "content" : str(isNull(user.age))},
                    {"labelname": '手机号', "content" : str(isNull(user.phonenumber))},
                    {"labelname": '地址', "content" : str(isNull(user.address))},
                    {"labelname": '血型', "content" : str(isNull(user.bloodtype))},
                    {"labelname": '生日', "content" : str(isNull(user.datebirth))},
                    {"labelname": '星座', "content" : str(isNull(user.constellation))},
                    {"labelname": '邮箱', "content" : str(isNull(user.mail))},
                    {"labelname": '生肖', "content" : str(isNull(user.shengxiao))},
                    {"labelname": '个性签名', "content" : str(isNull(user.sign))},
                    {"labelname": '职业', "content" : str(isNull(user.profession))},
                    {"labelname": '所处地区', "content" : str(isNull(user.region))}]
            })
        else:
            result=0
        return result

def getRecentmessage(ID):
    messageslist = Messageslist.objects.filter(userid=ID)
    result=[]
    for i in messageslist:
        user = User.objects.get(loginid=i.objectid)
        result.append({
            "id":user.loginid,
            "username": user.username,
            "headportrait": user.headportrait,
            "time": i.time[11:16]
        })
    return result

def getChatInfo(request):
    if request.method == "POST":
        friendid = request.POST.get("friendid")
        user = User.objects.get(loginid=int(friendid))
        if user:
            result =json.dumps({
            "username" : user.username,
            "headportrait" : user.headportrait,
            "id" : str(isNull(user.loginid)),
            "status":user.loginstatus,
            "Info" : [{"labelname": '性别', "content" : str(isNull(user.sex))},
                      # {"labelname": '年龄', "content" : str(isNull(user.age))},
                      {"labelname": '手机号', "content" : str(isNull(user.phonenumber))},
                      {"labelname": '地址', "content" : str(isNull(user.address))},
                      # {"labelname": '血型', "content" : str(isNull(user.bloodtype))},
                      {"labelname": '生日', "content" : str(isNull(user.datebirth))},
                      {"labelname": '星座', "content" : str(isNull(user.constellation))},
                      {"labelname": '邮箱', "content" : str(isNull(user.mail))},
                      # {"labelname": '生肖', "content" : str(isNull(user.shengxiao))},
                      {"labelname": '个性签名', "content" : str(isNull(user.sign))},
                      # {"labelname": '职业', "content" : str(isNull(user.profession))},
                      {"labelname": '所处地区', "content" : str(isNull(user.region))}]
            })
        else:
            result=0
        return result
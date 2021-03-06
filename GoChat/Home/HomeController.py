import datetime
import json
import os
import random
import time

import MySQLdb
import requests
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core import serializers
from django.db.models import Q
from users.models import User,UserInfo
from .models import Friends, FriendsGroup, Messageslist, Messages, Addfriends, Group, Groupmembers, AddGroups, \
    SecurityQuestion
from django.forms.models import model_to_dict
from urllib import parse



def EditSign(request): #编辑签名
    if request.method == "POST":
        NewSign=request.POST.get("NewSign")
        user = User.objects.get(loginid=request.COOKIES.get('LoginID'))
        user.sign=NewSign
        user.save()
        if(user != None):
            return True
        else:
            return False

def getFriendGroup(ID): #加载好友列表及好友列表
    friendsgroup = FriendsGroup.objects.filter(userid=ID).order_by('serialnumber')
    result=[]
    for i in friendsgroup:
        friends = Friends.objects.filter(userid=ID,friendgroupsid=i.groupid)
        children=[]
        for j in friends:
            friend=User.objects.get(loginid=j.friendid)
            children.append({
                "id":friend.loginid,
                "username":friend.username,
                "Remarkname":j.name,
                "headportrait":friend.headportrait,
                "sign":str(isNull(friend.sign))
            })
        result.append({
            "groupname": i.groupname,
            "serialnumber": i.serialnumber,
            "children": children,
            "number":len(children)
        })
    return result

def getGroups(ID): #获得群列表
    Groups = Groupmembers.objects.filter(userid=ID)
    Groupslist=[]
    Groupname=['我创建的群聊','我管理的群聊','我加入的群聊']
    role=['Groupleader','Administrators','Member']
    j=0
    for i in role:
        Groups1=Groups.filter(role=i).values()
        Count=Groups.filter(role=i).count()
        group=[]
        for k in list(Groups1):
            a=Group.objects.get(groupid=k['groupid'])
            group.append({'groupid':a.groupid, 'groupname':a.groupname,'serialnumber': j+1, 'Remarkname':isNull(k['groupname']),'groupavatars':a.groupavatars})
        Groupslist.append({'groupname': Groupname[j],'children':group,'Count':Count})
        j+=1

    return Groupslist

def getGroupslist(ID): #获得群列表
    Groups = Groupmembers.objects.filter(userid=ID)
    Groupslist=[]
    Groupname=['我创建的群聊','我管理的群聊','我加入的群聊']
    role=['Groupleader','Administrators','Member']
    j=0
    for i in role:
        Groups1=Groups.filter(role=i).values()
        Count=Groups.filter(role=i).count()
        group=[]
        for k in list(Groups1):
            a=Group.objects.get(groupid=k['groupid'])
            group.append({'groupid':a.groupid, 'groupname':a.groupname,'serialnumber': j+1, 'Remarkname':isNull(k['groupname']),'groupavatars':a.groupavatars})
        Groupslist.append({'groupname': Groupname[j],'children':group,'Count':Count})
        j+=1

    return {'status': 1, 'result': Groupslist}

def getFriends(ID): #获得好友列表
    friends = Friends.objects.filter(userid=ID)
    # friends=model_to_dict(friends)
    result={}
    j=0
    for i in friends:
        result[j]=model_to_dict(i)
        j+=1
    return result

def get_myInfo(user): #获取个人信息
    UserInfo.id = user.loginid
    UserInfo.username = user.username
    UserInfo.sex = user.sex
    UserInfo.age = user.age
    UserInfo.headportrait = user.headportrait
    UserInfo.phonenumber = user.phonenumber
    UserInfo.address = user.address
    UserInfo.bloodtype = user.bloodtype
    UserInfo.datebirth = user.datebirth[0:10]
    UserInfo.constellation = user.constellation
    UserInfo.mail = user.mail
    UserInfo.shengxiao = user.shengxiao
    UserInfo.sign = user.sign
    UserInfo.profession = user.profession
    UserInfo.region = user.region
    UserInfo.headercolor=user.headercolor
    return UserInfo

def getOneWord(): #一言功能
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


def EditUserName(request): #编辑用户名
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

def getSex(sex):
    if(sex=='1'):
        return "男"
    elif(sex=='2'):
        return "女"
    elif(sex=='3'):
        return "其他"
    else:
        return ""

def getrole(role):
    if(role=='Groupleader'):
        return "群主"
    elif(role=='Administrators'):
        return "管理员"
    elif(role=='Member'):
        return "成员"
    else:
        return ""

def getFriendInfo(request): #获得好友信息
    if request.method == "POST":
        UserID = request.COOKIES.get('LoginID')
        friendid = request.POST.get("friendid")
        user = User.objects.get(loginid=int(friendid))
        friends=Friends.objects.get(userid=UserID,friendid=friendid)
        if user:
            result =json.dumps({
            "Username" : user.username,
            "Userid":user.loginid,
            "Headportrait" : "/static/HeadPortrait/"+user.headportrait,
            "Remarkname":friends.name,
            "Sex":user.sex,
            "Age":user.age,
            "sign":user.sign,
            "friendgroupsid":friends.friendgroupsid,
            "Birthday":user.datebirth[5:11],
            "Constellation":user.constellation,
            "Shengxiao":user.shengxiao,
            "background": "background-color:" + user.headercolor,
            })
        else:
            result=0
        return result

def getobjectInfo(request): #获得用户信息
    if request.method == "POST":
        objectid = request.POST.get("objectid")
        result=""
        user = User.objects.get(loginid=objectid)
        if user:
            result ={
            "Username" : user.username,
            "Userid":user.loginid,
            "Headportrait" : user.headportrait,
            "Sex":user.sex,
            "Age":user.age,
            "sign":user.sign,
            "Birthday":user.datebirth[5:10],
            "Shengxiao":user.shengxiao,
            "background": "background-color:" + user.headercolor,
            }
        else:
            result=0
        return result

def getGroupInfo(request): #获得群组信息
    if request.method == "POST":
        UserID = request.COOKIES.get('LoginID')
        groupid = request.POST.get("groupid")
        group = Group.objects.get(groupid=int(groupid))
        groupmembers=Groupmembers.objects.get(userid=UserID,groupid=int(groupid))
        if group:
            groupmembers1 = Groupmembers.objects.filter(groupid=int(groupid)).values("userid","name","groupname","role","jointime","userid")
            members=[]
            memberlist=[]
            value=[]
            for i in  list(groupmembers1):
                members.append({
                    "userid":i['userid'],
                    "headportrait":User.objects.get(loginid=i['userid']).headportrait,
                    "username":User.objects.get(loginid=i['userid']).username,
                    "userremarks":i['name'],
                    "role":getrole(i['role']),
                    "jointime":i['jointime'][:11],
                })
                if i['role'] != 'Groupleader':
                    memberlist.append({
                        "label":User.objects.get(loginid=i['userid']).username,
                        "key":i['userid'],
                        # "disabled": True if i['role']=='Groupleader' else False
                    })
                if i['role']=='Administrators':
                    value.append(i['userid'])

            result =json.dumps({
                "groupname" : group.groupname,
                "groupid":group.groupid,
                "groupremarks":groupmembers.groupname,
                "userremarks": groupmembers.name,
                "groupavatars" : "/static/HeadPortrait/"+group.groupavatars,
                "groupintro":group.groupintro,
                "role": Groupmembers.objects.get(userid=UserID,groupid=int(groupid)).role,
                "groupverification":str(group.groupverification),
                "memberlist":memberlist,
                "value":value,
                "members" : members
            })
        else:
            result=0
        return result

def getNewMessages(userid,objectid,MessagesType):
    userid=str(userid)
    objectid=str(objectid)
    conn = MySQLdb.connect(host='localhost',user='root',password='123456',database='gochat',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sqlstr=""
    if MessagesType=='friend':
        sqlstr="SELECT PostMessages,SendTime FROM home_messages " \
                "WHERE FromUserID IN ("+userid+","+objectid+") and ToUserID IN ("+userid+","+objectid+") and MessagesType = '"+MessagesType+"' " \
                "order by SendTime DESC LIMIT 0,1"
    if MessagesType=='group':
        sqlstr="SELECT PostMessages,SendTime FROM home_messages " \
                "WHERE ToUserID = '"+objectid+"' and MessagesType = '"+MessagesType+"' " \
                "order by SendTime DESC LIMIT 0,1"
    try:
        # 执行SQL语句
        cursor.execute(sqlstr)
        Messages =cursor.fetchall()
        return Messages
    except Exception as e:
        # 有异常，回滚事务
        print("getNewMessages回滚")
        conn.rollback()
    cursor.close()
    conn.close()

def getRecentmessage(request): #获得最近会话
    ID=request.COOKIES.get('LoginID')
    messageslist = Messageslist.objects.filter(userid=ID).order_by('-time')
    result=[]
    for i in messageslist:
        if i.messagestype=='friend':
            user = User.objects.get(loginid=i.objectid)
            Messages=getNewMessages(ID,user.loginid,'friend')
            username=Friends.objects.get(userid=int(ID),friendid=user.loginid).name
            result.append({
                "id": user.loginid,
                "username": user.username if username==None or username=="" else username,
                "headportrait": user.headportrait,
                "messagestype":i.messagestype,
                "PostMessages": Messages[0]['PostMessages'] if len(Messages)>0 else ' ' ,
                "time": i.createtime[10:16] if i.time=="" else i.time[10:16],
                "unreadnum":i.unreadnum
            })
        elif i.messagestype=='group':
            group = Group.objects.get(groupid=i.objectid)
            Messages=getNewMessages(ID, group.groupid, 'group')
            groupname = Groupmembers.objects.get(userid=int(ID), groupid=group.groupid).groupname
            result.append({
                "id": group.groupid,
                "username": group.groupname if groupname==None or groupname=="" else groupname,
                "headportrait": group.groupavatars,
                "messagestype": i.messagestype,
                "PostMessages":Messages[0]['PostMessages'] if len(Messages)>0 else ' ' ,
                "time": Messages[0]['SendTime'][10:16] if len(Messages)>0 else '',
                "unreadnum": i.unreadnum
            })
    return result

def RefreshRecentmessage(request): #获得最近会话
    ID=request.COOKIES.get('LoginID')
    messageslist = Messageslist.objects.filter(userid=ID).order_by('-time')
    result=[]
    for i in messageslist:
        if i.messagestype == 'friend':
            user = User.objects.get(loginid=i.objectid)
            Messages = getNewMessages(ID, user.loginid, 'friend')
            username = Friends.objects.get(userid=int(ID), friendid=user.loginid).name
            result.append({
                "id": user.loginid,
                "username": user.username if username == None or username == "" else username,
                "headportrait": user.headportrait,
                "messagestype": i.messagestype,
                "PostMessages": Messages[0]['PostMessages'] if len(Messages) > 0 else ' ',
                "time": i.createtime[10:16] if i.time == "" else i.time[10:16],
                "unreadnum": i.unreadnum
            })
        elif i.messagestype == 'group':
            group = Group.objects.get(groupid=i.objectid)
            Messages = getNewMessages(ID, group.groupid, 'group')
            groupname = Groupmembers.objects.get(userid=int(ID), groupid=group.groupid).groupname
            result.append({
                "id": group.groupid,
                "username": group.groupname if groupname == "" or groupname==None else groupname,
                "headportrait": group.groupavatars,
                "messagestype": i.messagestype,
                "PostMessages": Messages[0]['PostMessages'] if len(Messages) > 0 else ' ',
                "time": Messages[0]['SendTime'][10:16] if len(Messages) > 0 else '',
                "unreadnum": i.unreadnum
            })
    return {'status':1,'result':result}

def getChatInfo(request): #获取聊天对象信息
    if request.method == "POST":
        objectid = request.POST.get("objectid")
        messagestype = request.POST.get("messagestype")
        result=""
        if messagestype =='friend':
            user = User.objects.get(loginid=int(objectid))
            if user:
                result ={
                "username" : user.username,
                "headportrait" : "/static/HeadPortrait/"+user.headportrait,
                "id" : str(isNull(user.loginid)),
                "status":user.loginstatus,
                "region":user.region,
                "phone":user.phonenumber,
                "email":user.mail,
                "address":user.address,
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
                }
            else:
                pass
        elif messagestype =='group':
            group = Group.objects.get(groupid=int(objectid))
            if group:
                groupmembers1 = Groupmembers.objects.filter(groupid=int(objectid)).values("userid", "name", "groupname","role", "jointime")
                members = []
                for i in list(groupmembers1):
                    members.append({
                        "headportrait": User.objects.get(loginid=i['userid']).headportrait,
                        "username": User.objects.get(loginid=i['userid']).username,
                        "userremarks": i['name'],
                        "role": getrole(i['role'])
                    })
                result = {
                    "groupname": group.groupname,
                    "headportrait": "/static/HeadPortrait/" + group.groupavatars,
                    "groupid": str(isNull(group.groupid)),
                    "Info": group.groupintro,
                    "groupleaderid": group.groupleaderid,
                    "members": members
                }
            else:
                pass
        return result

def EditUserInfo(request): #编辑个人信息
    UserInfo = request.body.decode("utf-8")
    UserID = request.COOKIES.get('LoginID')
    UserInfo = json.loads(UserInfo)
    UserInfo=UserInfo.get('UserInfo')
    user = User.objects.get(loginid=UserID)
    user.age = UserInfo.get('UserAge') if UserInfo.get('UserAge')!=None else 0
    user.sex = isNull(UserInfo.get('UserSex'))
    user.phonenumber = isNull(UserInfo.get('UserPhone'))
    user.address = isNull(UserInfo.get('UserAddress'))
    user.bloodtype = isNull(UserInfo.get('UserBloodType'))
    user.datebirth = isNull(UserInfo.get('UserDateBirth'))
    user.constellation = isNull(UserInfo.get('UserConstellation'))
    user.shengxiao = isNull(UserInfo.get('UserShengXiao'))
    user.profession = isNull(UserInfo.get('UserProfession'))
    user.region = isNull(UserInfo.get('UserRegion'))
    user.mail = isNull(UserInfo.get('UserMail'))
    user.save()
    if (user != None):
        return True
    else:
        return False

def Find_friends(str): #查询好友
    if(str.isdigit()):
        user = User.objects.filter(Q(loginid=str)|Q(username__contains=str)).values('loginid','username','sex','age','headportrait','region')
    else:
        user = User.objects.filter(username__contains=str).values('loginid','username','sex','age','headportrait','region')
    if user.exists():
        return {'status':1,'result':list(user)}
    else:
        return {'status':0,'result':'未搜索到相关结果'}

def Find_groups(str): #查询群组
    if(str.isdigit()):
        groups = Group.objects.filter(Q(groupid=str)|Q(groupname__contains=str)).values()
    else:
        groups = Group.objects.filter(groupname__contains=str).values()
    if groups.exists():
        return {'status':1,'result':list(groups)}
    else:
        return {'status':0,'result':'未搜索到相关结果'}

def EditAvatar(request): #编辑头像
    UserID = request.COOKIES.get('LoginID')
    user = User.objects.get(loginid=UserID)
    img = request.FILES.get('img_file')
    timeid = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join([str(random.randint(1, 10)) for i in range(5)])  # 生成唯一的时间序列
    img_name = request.POST.get('img_name')
    img_name = img_name.split('.')
    img_name[0]=timeid
    OldHeadPortrait=settings.MEDIA_ROOT+"/HeadPortrait/"+user.headportrait
    HeadPortrait=img_name[0]+'.'+img_name[1]
    url = settings.MEDIA_ROOT+"/HeadPortrait/"+HeadPortrait

    with open(url, 'wb') as f:
        for chunk in img.chunks():
            f.write(chunk)

    if os.path.exists(OldHeadPortrait):
        os.remove(OldHeadPortrait)
    else:
        print("The file does not exist")

    user.headportrait = HeadPortrait
    user.save()
    if (user != None):
        return {'status':1,'result':'图片上传成功'}
    else:
        return {'status':0,'result':'图片上传失败'}

def getFriendGroups(request): #获取好友分组选项（添加好友时）
        UserID = request.COOKIES.get('LoginID')
        FriendGroups= FriendsGroup.objects.filter(userid=UserID).order_by("serialnumber").values()
        if FriendGroups.exists():
            FriendGroups=list(FriendGroups)
            options=[]
            for i in FriendGroups:
                options.append({'value':i['groupid'],'label':i['groupname'],'serial':i['serialnumber']})
            return options
        else:
            pass

def getAddFriend_applylist(request):
    UserID = request.COOKIES.get('LoginID')
    addfriends1 = Addfriends.objects.filter(userid=UserID).exclude(rep_results=2)
    addfriends2 = Addfriends.objects.filter(objectid=UserID).exclude(rep_results=2)
    AddFriend_applylist=addfriends1|addfriends2
    AddFriend_applylist=AddFriend_applylist.order_by("-sendtime").values("applicantid", "userid", "objectid", "addway", "remarks", "rep_results", "responsetime", "sendtime")
    a=[]
    for i in list(AddFriend_applylist):
        if i['objectid']==int(UserID):
            user=User.objects.get(loginid=i['userid'])
            b = {
                "applicantid": i['applicantid'],
                "headportrait": user.headportrait,
                "username":user.username,
                "objectid": i['userid'],
                "addway": i['addway'],
                "remarks": i['remarks'],
                "rep_results": i['rep_results'],
                "responsetime": i['responsetime'],
                "sendtime": i['sendtime'][:16],
                "state":'receive'
            }
        else:
            user = User.objects.get(loginid=i['objectid'])
            b = {
                "applicantid": i['applicantid'],
                "headportrait": user.headportrait,
                "username": user.username,
                "objectid": i['objectid'],
                "addway": i['addway'],
                "remarks": i['remarks'],
                "rep_results": i['rep_results'],
                "responsetime": i['responsetime'],
                "sendtime": i['sendtime'][:16],
                "state":'send'
            }
        a.append(b)
    if AddFriend_applylist.exists():
        return {'status': 1, 'result': a}
    else:
        return {'status': 0, 'result': '暂无申请'}

def getAddGroup_applylist(request):
    UserID = request.COOKIES.get('LoginID')
    # Groups = Groupmembers.objects.filter(userid=UserID,role__in=('Groupleader','Administrators')).exclude(rep_results=2).values('groupid')
    Groups = Groupmembers.objects.filter(userid=UserID,role__in=('Groupleader','Administrators')).values('groupid')
    group=[]
    for i in Groups:
        group.append(i['groupid'])
    applicant = AddGroups.objects.filter(objectid__in=group)
    AddGroup_applylist=applicant.order_by("-sendtime").values("applicantid", "userid", "objectid", "addway", "remarks", "sendtime", "rep_results", "responsetime","processorid")
    a=[]
    for i in list(AddGroup_applylist):
        if i['userid']==int(UserID):
            group = Group.objects.get(groupid=i['objectid'])
            b = {
                "applicantid": i['applicantid'],
                "headportrait": group.groupavatars,
                "name": group.groupname,
                "objectid": i['objectid'],
                "addway": i['addway'],
                "remarks": i['remarks'],
                "rep_results": i['rep_results'],
                "responsetime": i['responsetime'],
                "sendtime": i['sendtime'][:16],
                "state": 'send'
            }
        else:
            user = User.objects.get(loginid=i['userid'])
            b = {
                "applicantid": i['applicantid'],
                "headportrait": user.headportrait,
                "name": user.username,
                "groupname": Group.objects.get(groupid=i['objectid']).groupname,
                "objectid": i['userid'],
                "addway": i['addway'],
                "remarks": i['remarks'],
                "rep_results": i['rep_results'],
                "responsetime": i['responsetime'],
                "sendtime": i['sendtime'][:16],
                "state": 'receive'
            }
        a.append(b)
    if AddGroup_applylist.exists():
        return {'status': 1, 'result': a}
    else:
        return {'status': 0, 'result': '暂无申请'}

def verificat_isfriend(request):
    UserID = request.COOKIES.get('LoginID')
    friendid = request.POST.get("friendid")
    friendlist=Friends.objects.filter(userid=UserID)
    friend = friendlist.filter(friendid=friendid)
    if(len(friend) >0):
        return True
    else:
        return False

def Processing_requests(request): #处理添加请求
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form=json.loads(form)
    response = form.get('response')
    formAddfriend = form.get('formAddfriend')
    type = form.get('type')
    Applicant=""
    if type == "friend":
        Applicant = Addfriends.objects.get(applicantid=formAddfriend['applicantid'])
    elif type == "group":
        Applicant = AddGroups.objects.get(applicantid=formAddfriend['applicantid'])
    if Applicant!=None:
        if response=="agree":
            if type=="friend":
                friend=Friends.objects.filter(userid=UserID,friendid=Applicant.userid)
                print(friend)
                if len(friend)>0:
                    return {'status': 0, 'result': '好友已存在'}
                else:
                    Applicant.rep_results = 1
                    Applicant.responsetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    Friendship = []
                    Friendship.append(Friends(
                        userid=Applicant.userid,
                        friendid=Applicant.objectid,
                        name=Applicant.remarksname,
                        friendtypeid=1,
                        friendgroupsid=Applicant.friendsGroupid
                    ))
                    Friendship.append(Friends(
                        userid=UserID,
                        friendid=Applicant.userid,
                        name=formAddfriend['remarksname'],
                        friendtypeid=1,
                        friendgroupsid=formAddfriend['FriendGroups_value']
                    ))
                    Friends.objects.bulk_create(Friendship)
            elif type=="group":
                groupmembers = Groupmembers.objects.filter(userid=Applicant.userid, groupid=Applicant.objectid)
                if len(groupmembers) > 0:
                    return {'status': 0, 'result': '该用户已在群内'}
                else:
                    Applicant.rep_results = 1
                    Applicant.responsetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    Groupmembers.objects.create(
                        userid=Applicant.userid,
                        groupid=Applicant.objectid,
                        role='Member',
                        jointime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    )
        elif response=="refuse":
            Applicant.rep_results = -1
            Applicant.responsetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        elif response=="ignore":
            Applicant.rep_results = 2
            Applicant.responsetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        Applicant.save()
        if (Applicant != None):
            return {'status': 1, 'result': '操作成功'}
        else:
            return {'status': 0, 'result': '操作失败'}
    else:
        return {'status': 0, 'result': '非法操作'}

def ChangePassword(request):
    UserID = request.COOKIES.get('LoginID')
    Oldpassword = request.POST.get("Oldpassword")
    Newpassword = request.POST.get("Newpassword")
    if (Newpassword =='' or Oldpassword ==''):
        return {'status': 0, 'result': '密码不能为空'}
    elif (len(Newpassword) < 6 or len(Newpassword) > 16):
        return {'status': 0, 'result': '密码长度为6-16字符'}
    user = User.objects.get(loginid=UserID)
    result = check_password(Oldpassword, user.password)
    if result:
        user.password=make_password(Newpassword)
        user.save()
        return {'status': 1, 'result': '修改成功'}
    else:
        return {'status': 0, 'result': '原密码错误'}

def NewSession(request):
    UserID = request.COOKIES.get('LoginID')
    messagestype = request.POST.get("messagestype")
    objectid = request.POST.get("objectid")
    object=''
    result=''
    if(messagestype=='friend'):
        object=Friends.objects.filter(userid=UserID,friendid=objectid)
        user = User.objects.get(loginid=objectid)
        Messages = getNewMessages(UserID, user.loginid, 'friend')
        # print(len(Messages))
        result={
            "id": user.loginid,
            "username": user.username,
            "headportrait": user.headportrait,
            "messagestype": 'friend',
            "PostMessages": Messages[0]['PostMessages'] if len(Messages)>0 else '',
            "time": Messages[0]['SendTime'][10:16] if len(Messages)>0 else time.strftime('%H:%M', time.localtime())
        }
    elif(messagestype=='group'):
        object=Groupmembers.objects.filter(userid=UserID,groupid=objectid)
        group = Group.objects.get(groupid=objectid)
        Messages = getNewMessages(UserID, group.groupid, 'group')
        # print(len(Messages))
        result={
            "id": group.groupid,
            "username": group.groupname,
            "headportrait": group.groupavatars,
            "messagestype": 'group',
            "PostMessages": Messages[0]['PostMessages'] if len(Messages)>0 else '' ,
            "time": Messages[0]['SendTime'][10:16] if len(Messages)>0 else time.strftime('%H:%M', time.localtime())
        }
    if len(object)>0:
        Session=Messageslist.objects.filter(userid=UserID,objectid=objectid,messagestype=messagestype)
        if len(Session)==0:
            Messageslist.objects.create(
                userid=UserID,
                objectid=objectid,
                messagestype=messagestype,
                createtime=time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()),
                time=time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
            )
            return {'status': 1, 'result': result}
        else:
            return {'status': -1, 'result': '会话已存在'}
    else:
        return {'status': 0, 'result': '非法操作'}

def DeleteSession(request):
    UserID = request.COOKIES.get('LoginID')
    messagestype = request.POST.get("messagestype")
    objectid = request.POST.get("objectid")
    object = ''
    if (messagestype == 'friend'):
        object = Friends.objects.filter(userid=UserID, friendid=objectid)
    elif (messagestype == 'group'):
        object = Groupmembers.objects.filter(userid=UserID, groupid=objectid)
    # if not object.exists():
    if len(object)>0:
        Session = Messageslist.objects.filter(userid=UserID, objectid=objectid, messagestype=messagestype)
        if len(Session)>0:
            Session.delete()
            return {'status': 1, 'result': '会话删除成功'}
        else:
            return {'status': 0, 'result': '会话已存在'}
    else:
        return {'status': 0, 'result': '非法操作'}

def DeleteFriend(request):
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    friends = Friends.objects.filter(userid=UserID, friendid=objectid)
    # if not object.exists():
    if len(friends)>0:
        Session = Friends.objects.filter(userid__in=(UserID,objectid), friendid__in=(UserID,objectid))
        if len(Session)>0:
            Session.delete()
            return {'status': 1, 'result': '好友删除成功'}
        else:
            return {'status': 0, 'result': '好友不存在'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditFriendname(request):
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    Newname = request.POST.get("Newname")
    friends = Friends.objects.get(userid=UserID, friendid=objectid)
    if friends!=None:
    # if len(friends) > 0:
        friends.name=Newname
        friends.save()
        return {'status': 1, 'result': '备注修改成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditGroupname(request): #修改群备注
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    remarkname = request.POST.get("remarkname")
    group = Groupmembers.objects.get(userid=UserID, groupid=objectid)
    if group!=None:
    # if len(friends) > 0:
        group.groupname=remarkname
        group.save()
        return {'status': 1, 'result': '备注修改成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditGroupUserremarks(request): #修改群内备注
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    remarkname = request.POST.get("remarkname")
    group = Groupmembers.objects.get(userid=UserID, groupid=objectid)
    if group!=None:
    # if len(friends) > 0:
        group.name=remarkname
        group.save()
        return {'status': 1, 'result': '备注修改成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditFriendGroup(request):
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    friendgroupid = request.POST.get("FriendGroupid")
    friends = Friends.objects.get(userid=UserID, friendid=objectid)
    if friends!=None:
    # if len(friends) > 0:
        friends.friendgroupsid=friendgroupid
        friends.save()
        return {'status': 1, 'result': '分组修改成功'}
    else:
        return {'status': 0, 'result': '非法操作'}


def MoveFriendGroup(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    groupid = form.get('groupid')
    serial = form.get('serial')
    friendsgroup = FriendsGroup.objects.filter(groupid__in=groupid, userid=UserID)
    if friendsgroup.count()>0:
        j=0
        for i in groupid:
            F=FriendsGroup.objects.get(groupid=i)
            F.serialnumber=serial[j]
            F.save()
            j=j+1
        return {'status': 1, 'result': '分组移动成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def AddFriendGroup(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    label = form.get('label')
    serial = form.get('serial')
    createtime='{0:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
    FriendsGroup.objects.create(
        userid=UserID,
        groupname=label,
        serialnumber=serial,
        createtime=createtime
    )
    new=FriendsGroup.objects.get(createtime=createtime)
    return {'status': 1, 'result': '分组添加成功','groupid':new.groupid}

def DeleteFriendGroup(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    groupid = form.get('groupid')
    friendsgroup=FriendsGroup.objects.filter(groupid=groupid,userid=UserID)
    if friendsgroup.count()>0:
        Count=Friends.objects.filter(friendgroupsid=groupid).count()
        if Count==0:
            friendsgroup.delete()
            return {'status': 1, 'result': '分组删除成功'}
        else:
            return {'status': 0, 'result': '分组不为空操作失败'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditFriendGroupname(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    groupid = form.get('groupid')
    label = form.get('label')
    friendsgroup=FriendsGroup.objects.get(groupid=groupid,userid=UserID)
    if friendsgroup!=None:
        friendsgroup.groupname=label
        friendsgroup.save()
        return {'status': 1, 'result': '分组编辑成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditHeaderstyle(request):
    UserID = request.COOKIES.get('LoginID')
    background = request.POST.get("background")
    user = User.objects.get(loginid=UserID)
    user.headercolor=background
    user.save()
    return {'status': 1, 'result': '修改成功'}

def Editgroupverification(request):
    UserID = request.COOKIES.get('LoginID')
    type = request.POST.get("type")
    objectid = request.POST.get("objectid")
    groupmembers = Groupmembers.objects.filter(userid=UserID,groupid=objectid,role__in=('Groupleader','Administrators'))
    if len(groupmembers)>0:
        group=Group.objects.get(groupid=objectid)
        group.groupverification=type
        group.save()
        return {'status': 1, 'result': '修改成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def Disbandgroup(request):
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    groupmembers = Groupmembers.objects.filter(userid=UserID,groupid=objectid,role='Groupleader')
    if len(groupmembers)>0:
        group=Group.objects.get(groupid=objectid)
        group.delete()
        return {'status': 1, 'result': '解散成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def Exitgroup(request):
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get("objectid")
    groupmembers = Groupmembers.objects.filter(userid=UserID,groupid=objectid,role__in=('Administrators','Member'))
    if len(groupmembers)>0:
        group=Groupmembers.objects.get(userid=UserID,groupid=objectid)
        group.delete()
        return {'status': 1, 'result': '退出成功'}
    else:
        return {'status': 0, 'result': '非法操作'}

def SetupAdmin(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    NewAdmin = form.get('NewAdmin')
    objectid = form.get('objectid')
    print(NewAdmin)
    groupmembers = Groupmembers.objects.filter(userid=UserID,groupid=objectid,role='Groupleader')
    if len(groupmembers)>0:
        members=Groupmembers.objects.exclude(userid__in=NewAdmin).exclude(role='Groupleader').filter(groupid=objectid)
        members.update(**{'role':'Member'})
        admin = Groupmembers.objects.filter(groupid=objectid,userid__in=NewAdmin)
        admin.update(**{'role':'Administrators'})
        return {'status': 1, 'result': '完成操作'}
    else:
        return {'status': 0, 'result': '非法操作'}

def RemoveMembers(request):
    UserID = request.COOKIES.get('LoginID')
    form = request.body.decode("utf-8")
    form = json.loads(form)
    Members = form.get('Members')
    objectid = form.get('objectid')
    members=[]
    for i in Members:
        members.append(i['userid'])
    groupmembers = Groupmembers.objects.filter(userid=UserID,groupid=objectid,role__in=('Groupleader','Administrators'))
    if len(groupmembers)>0:
        user=Groupmembers.objects.filter(userid__in=members,groupid=objectid)
        user.delete()
        return {'status': 1, 'result': '完成操作'}
    else:
        return {'status': 0, 'result': '非法操作'}

def EditProfile(request): #编辑群资料
    UserID = request.COOKIES.get('LoginID')
    objectid = request.POST.get('objectid')
    img_name = request.POST.get('img_name')
    groupname=request.POST.get('groupname')
    groupintro = request.POST.get('groupintro')
    if groupname=="":
        return {'status': 0, 'result': '群名不能为空'}
    if img_name!="":
        groupmembers = Groupmembers.objects.filter(userid=UserID, groupid=objectid,role__in=('Groupleader', 'Administrators'))
        if len(groupmembers)>0:
            group = Group.objects.get(groupid=objectid)
            img = request.FILES.get('img_file')
            timeid = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join([str(random.randint(1, 10)) for i in range(5)])  # 生成唯一的时间序列
            img_name = img_name.split('.')
            img_name[0]=timeid
            OldHeadPortrait=settings.MEDIA_ROOT+"/HeadPortrait/"+group.groupavatars
            HeadPortrait=img_name[0]+'.'+img_name[1]
            url = settings.MEDIA_ROOT+"/HeadPortrait/"+HeadPortrait

            with open(url, 'wb') as f:
                for chunk in img.chunks():
                    f.write(chunk)

            if os.path.exists(OldHeadPortrait):
                os.remove(OldHeadPortrait)
            else:
                print("The file does not exist")
            group.groupavatars = HeadPortrait
            group.groupname=groupname
            group.groupintro=groupintro
            group.save()
            if (group != None):
                return {'status':1,'result':'编辑成功'}
            else:
                return {'status':0,'result':'编辑失败'}
        else:
            return {'status':0,'result':'非法操作'}
    else:
        groupmembers = Groupmembers.objects.filter(userid=UserID, groupid=objectid,
                                                   role__in=('Groupleader', 'Administrators'))
        if len(groupmembers) > 0:
            group = Group.objects.get(groupid=objectid)
            group.groupname = groupname
            group.groupintro = groupintro
            group.save()
            if (group != None):
                return {'status': 1, 'result': '编辑成功'}
            else:
                return {'status': 0, 'result': '编辑失败'}
        else:
            return {'status':0,'result':'非法操作'}

def SearchFriend(request):
    UserID = request.COOKIES.get('LoginID')
    content=request.POST.get('content')
    conn = MySQLdb.connect(host='localhost', user='root', password='123456', database='gochat',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sqlstr = "SELECT `user`.LoginID userid, home_friends.`Name`, `user`.UserName, `user`.HeadPortrait, `user`.Sign " \
             "FROM `user` INNER JOIN home_friends ON  `user`.LoginID = home_friends.FriendID " \
             "WHERE home_friends.UserID = "+UserID+" and (`user`.UserName LIKE '%"+content+"%' or `user`.LoginID LIKE '%"+content+"%' or home_friends.`Name` LIKE '%"+content+"%' )"
    try:
        # 执行SQL语句
        cursor.execute(sqlstr)
        user = cursor.fetchall()
    except Exception as e:
        conn.rollback()
    cursor.close()
    conn.close()
    print(user)
    # friends= Friends.objects.filter(userid=UserID)
    # friendlist=[]
    # for i in friends:
    #     friendlist.append(i.friendid)
    # user = User.objects.filter(Q(loginid__in=friendlist),Q(loginid__contains=content) | Q(username__contains=content)).values('loginid', 'username', 'headportrait', 'sign')
    # # if (content.isdigit()):
    # #     user = User.objects.filter(Q(loginid__in=friendlist),Q(loginid__contains=content) | Q(username__contains=content)).values('loginid', 'username', 'headportrait', 'sign')
    # # else:
    # #     user = User.objects.filter(username__contains=str).values('loginid', 'username', 'headportrait','sign')
    # if user.exists():
    return {'status': 1, 'result': user}
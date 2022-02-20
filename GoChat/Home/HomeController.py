import requests
from users.models import User,UserInfo
from Home.models import Friends
from django.forms.models import model_to_dict


def EditSign(request):
    if request.method == "POST":
        NewSign=request.POST.get("NewSign")
        user = User.objects.get(loginid=request.COOKIES.get('LoginID'))
        user.sign=NewSign
        if(user.save()):
            return True
        else:
            return False

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

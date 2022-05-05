import json
import random
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from . import models
from django.shortcuts import render
from .models import User
from Home.models import SecurityQuestion


@csrf_exempt
def Register(request):
    if request.method == "POST":
        addtimeid = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join([str(random.randint(1, 10)) for i in range(5)]) #生成唯一的时间序列
        status = 0
        ID = None
        form = request.body.decode("utf-8")
        form = json.loads(form)
        NickName=form.get('NickName')
        PassWord = form.get('PassWord')
        RePassWord = form.get('RePassWord')
        question1 = form.get('question1')
        question2 = form.get('question2')
        answer1 = form.get('answer1')
        answer2 = form.get('answer2')
        if (NickName == ""):
            tip = "用户名不能为空！"
        elif (PassWord == ""):
            tip = "密码不能为空！"
        elif (len(PassWord) < 6 or len(PassWord) > 16):
            tip = "密码长度应为6-16字符"
        elif (RePassWord == ""):
            tip = "两次密码不一样！"
        elif (RePassWord !=PassWord):
            tip = "两次密码不一样！"
        elif (question1 =='' or question2 ==''):
            tip = "密保问题未设置！"
        elif (answer1 =='' or answer2 ==''):
            tip = "密保答案未设置！"
        else:
            PassWord = make_password(PassWord)
            models.User.objects.create(
                username=NickName,
                password=PassWord,
                addtimeid=addtimeid,
                datebirth='1900-01-01T16:00:00.000Z',
                question1=question1,
                question2=question2,
                answer1=answer1,
                answer2=answer2,
            )
            status = 1
            tip = "注册成功！"
            user = models.User.objects.get(addtimeid=addtimeid)
            ID = user.loginid
        if (ID is not None):
            return HttpResponse(json.dumps({
                "status": status,
                "result": tip,
                "ID": ID
            }))
        else:
            return HttpResponse(json.dumps({
                "status": status,
                "result": tip,
            }))
    return render(request, 'Account/Register.html',{"QuestionList":getSecurityQuestion()})

@csrf_exempt
def Login(request):
    if request.method == "POST":
        status = 0
        LoginID = request.POST.get("LoginID")
        PassWord = request.POST.get("PassWord")
        next_url = request.GET.get("next")
        if (LoginID.isdigit() == False):
            tip = "账号只能为数字"
        elif (Verify_LoginID(LoginID)):
            tip = "账号不存在"
        else:
            # user = models.User.objects.filter(loginid=LoginID, password=PassWord)
            user = models.User.objects.get(loginid=LoginID)
            result=check_password(PassWord,user.password)
            if result:
                status = 1
            else:
                tip = "密码不正确"
        if (status == 1):
            Response = HttpResponse(json.dumps({
                "status": status,
                "url": "Home/Recent_chat/"}))
            if next_url:
                Response = HttpResponse(json.dumps({
                    "status": status,
                    "url": next_url}))
            Response.set_cookie('LoginID', LoginID)
            return Response
        else:
            return HttpResponse(json.dumps({
                "status": status,
                "result": tip,
            }))
    return render(request, 'Account/Login.html')

def Logout(request):
    response = HttpResponseRedirect('/Login')
    #清理cookie里保存username
    logout(request)
    response.delete_cookie('LoginID')
    return response

def Verify_Phone(phonenumber):  # 验证手机号唯一性
    if (models.User.objects.filter(phonenumber=phonenumber)):
        return True
    else:
        return False

def Verify_LoginID(LoginID):  # 验证账号是否存在
    # try:
    #     user=models.User.objects.get(loginid=LoginID)
    # except models.User.DoesNotExist:
    #     user = None
    user = models.User.objects.filter(loginid=LoginID)
    # if (user == None):
    if user:
        return False #账号不存在
    else:
        return True



def dashboard(request):
    user_count = User.objects.count()
    user_online = User.objects.filter(loginstatus=1).count()
    context = { 'user_count': user_count,
                'user_online': user_online,}
    return render(request, 'admin/dashboard.html',context)

def getSecurityQuestion():
    QuestionList=SecurityQuestion.objects.all().values()
    result=[]
    for i in QuestionList:
        result.append({
            'value':i['questionid'],
            'label':i['question']
        })
    return result
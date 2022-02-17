import json
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import datetime
from . import models

@csrf_exempt
def Register(request):
    if request.method == "POST":
        addtimeid = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join([str(random.randint(1, 10)) for i in range(5)])
        status = 0
        ID = None
        NickName = request.POST.get("NickName")
        PassWord = request.POST.get("PassWord")
        Telephone = request.POST.get("Telephone")
        if (NickName == ""):
            tip = "用户名不能为空！"
        elif (PassWord == ""):
            tip = "密码不能为空！"
        elif (Telephone == ""):
            tip = "手机号不能为空！"
        elif (Verify_Phone(Telephone)):
            tip = "手机号已被使用！"
        else:
            models.User.objects.create(
                username=NickName,
                password=PassWord,
                phonenumber=Telephone,
                addtimeid=addtimeid
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
    return render(request, 'Account/Register.html')

@csrf_exempt
def Login(request):
    if request.method == "POST":
        status = 0
        LoginID = request.POST.get("LoginID")
        PassWord = request.POST.get("PassWord")
        if (LoginID.isdigit() == False):
            tip = "账号只能为数字"
        elif (Verify_LoginID(LoginID)):
            tip = "账号不存在"
        else:
            user = models.User.objects.filter(loginid=LoginID, password=PassWord)
            if user:
                status = 1
            else:
                tip = "密码不正确"
        if (status == 1):
            Response = HttpResponse(json.dumps({
                "status": status,
                "url":"Home/Recent_chat/"}))
            Response.set_cookie('LoginID', LoginID, 3600)
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


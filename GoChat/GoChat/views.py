from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# def Login(request):
#     return render(request, "Account/Login.html")
#
#
# def Register(request):
#     return render(request, "Account/Register.html")

def Home(request):
    # LoginID = request.COOKIES.get('LoginID', '')
    # if(LoginID==""):
    #     return HttpResponseRedirect("/Account/LoginView")
    return redirect("Home/Recent_chat/")


def Friends_list(request):
    return render(request, "Home/Friends_list.html")


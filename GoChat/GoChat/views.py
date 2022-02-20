from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def Home(request):
    return redirect("Home/Recent_chat/")


def Friends_list(request):
    return render(request, "Home/Friends_list.html")


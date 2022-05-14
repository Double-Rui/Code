from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from Home.views import Recent_chat

def Home(request):
    return Recent_chat(request)
    # return redirect("GoChat/")


def Friends_list(request):
    return render(request, "Home/Friends_list.html")


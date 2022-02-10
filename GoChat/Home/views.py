from django.shortcuts import render

# Create your views here.
def Recent_chat(request):
    return render(request, "Home/Recent_chat.html")

def Friends_list(request):
    return render(request, "Home/Friends_list.html")

def Find_Friends(request):
    return render(request, "Home/Find_Friends.html")


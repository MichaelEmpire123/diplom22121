from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'main/index.html')

def chat(req):
    return render(req, 'chat/chat.html')

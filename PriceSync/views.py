from django.shortcuts import render
from django.http import HttpResponse

# create your views here
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello World")

def login(request):
    return render(request, 'login.html')

def forgotpassword(request):
    return render(request, 'forgot-password.html')

def signup(request):
    return render(request, 'signup.html')

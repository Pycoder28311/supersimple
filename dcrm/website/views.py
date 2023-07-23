from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')
# Create your views here.
#def home(request):
    #return HttpResponse('<div class="col-md-6 offset-md-3"><h1>hello everyone</h1>')

#def loginuser(request):
    #pass

#def logoutuser(request):
    #pass

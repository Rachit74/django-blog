from django.shortcuts import render
from django.http import HttpResponse

#views

def home(request):
    return render(request,'blog/home.html')

def about(request):
    return HttpResponse("Blog About")

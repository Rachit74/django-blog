from django.shortcuts import render
from django.http import HttpResponse

#views

def home(request):
    return HttpResponse("Blog App")

def about(request):
    return HttpResponse("Blog About")

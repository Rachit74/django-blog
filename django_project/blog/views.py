from django.shortcuts import render
from django.http import HttpResponse

# dummy data

posts = [
    {
        'id': 1,
        'name': 'Rachit',
        'content': 'Hello There!',
    },
    {
        'id': 2,
        'name': 'TestUser1',
        'content': 'Hello',
    },
    {
        'id': 3,
        'name': 'TestUser2',
        'content': 'There Hello',
    },
]

#views

def home(request):
    context = {
        'posts': posts,
    }
    return render(request,'blog/home.html', context=context)

def about(request):
    return render(request, "blog/about.html")

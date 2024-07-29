from django.shortcuts import render
from django.http import HttpResponse

# dummy data

posts = [
    {
        'id': 1,
        'title': 'Blog1',
        'author': 'User1',
        'content': 'Hello There!',
        'date': '1st june, 1936, 19:45',
    },
    {
        'id': 2,
        'title': 'Blog2',
        'author': 'User2',
        'content': 'Hello There!',
        'date': '4 june, 2024, 13:43',
    },
    {
        'id': 3,
        'title': 'Blog3',
        'author': 'User3',
        'content': 'Hello There!',
        'date': '16 Decenber, 1971, 20:00',
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

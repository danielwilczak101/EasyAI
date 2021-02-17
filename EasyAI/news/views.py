from django.shortcuts import render
from django.http import HttpResponse

postsDic = [
    {
        'author': 'admin',
        'title': 'News Post 1',
        'content': 'Test Post content',
        'date_posted': 'August, 27, 2021'
    },
    {
        'author': 'admin2',
        'title': 'News Post 2',
        'content': 'Test Post content2',
        'date_posted': 'August, 28, 2021'
    }
]

def home(request):
    context = {
        'posts': postsDic
    }
    return render(request, 'news/home.html', context)
    
def about(request):
    return render(request, 'news/about.html', {'title': 'About'})

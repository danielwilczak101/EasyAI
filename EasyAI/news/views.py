from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'news/home.html', context)
    
def about(request):
    return render(request, 'news/about.html', {'title': 'About'})

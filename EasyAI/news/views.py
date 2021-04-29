from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from EasyGA import GA

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'news/home.html', context)
    
def about(request):
    return render(request, 'news/about.html', {'title': 'About'})
    
def form(request):
    ga = GA()
    a=1 #this number determines how many evolutions there are, will be changed later using form
    ga.evolve(a)
    context = {
        'population': ga.population,
        'best': ga.population[0]
    }
    return render(request, 'news/form.html',context)
    
def easyga(request):
    ga = GA()
    a=1 #this number determines how many evolutions there are, will be changed later using form
    ga.evolve(a)
    context = {
        'population': ga.population,
        'best': ga.population[0]
    }
    return render(request, 'news/easyga.html', context)

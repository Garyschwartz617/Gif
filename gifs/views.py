from django.shortcuts import render
from .models import *
# Create your views here.

def homepage(request):
    gifs = Gif.objects.all()
    context = {'gifs': gifs}
    return render(request,'index.html', context)

def category(request, wrd):
    gifs = Category.objects.get(name = wrd)
    # gifs =Gif.category_set.filter(name = wrd)
    context = {'g': gifs}
    return render(request,'category.html', context)

def categories(request):
    cat = Category.objects.all()
    context = {'cat': cat}
    return render(request,'categories.html', context)

def gif(request, num):
    g = Gif.objects.get(id = num)
    # l = Like.objects.create(gif = num)    
    context = {'gif': g, 'like': l}
    return render(request,'gif.html', context)



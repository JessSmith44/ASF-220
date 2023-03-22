from django.shortcuts import render
from templates import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def random(request):
    return render(request, 'random.html')

def gallery(request):
    return render(request, 'gallery.html')

def admin(request):
    return render(request, 'admin.html')
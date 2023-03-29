from django.shortcuts import render
import sys
sys.path.append("..")
from .templates import *
from .models import UploadImage

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def random(request):
    return render(request, 'random.html')

def gallery(request):
    pics =UploadImage.objects.all()
    return render(request, 'gallery.html',{"pics":pics})

def admin(request):
    return render(request, 'admin.html')
from django.urls import path
from .views import home, about, random, gallery, admin

urlpatterns = [
    path('home.html', home, name='home'),
    path('about.html', about, name='about'),
    path('random.html', random, name='random'),
    path('gallery.html', gallery, name='gallery'),
    path('admin.html', admin, name='admin')
]
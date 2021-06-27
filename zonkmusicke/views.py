from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeLanding,HomeAbout, HomeShows

# Create your views here.
def home(request):
    homland = HomeLanding.get_homelanding()
    homabout = HomeAbout.get_homeabout()
    homshows = HomeShows.get_homeshows()
    return render(request,'home.html', { "homland":homland , "homabout":homabout, "homshows":homshows})

def shows(request):
    return render(request, 'shows.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')
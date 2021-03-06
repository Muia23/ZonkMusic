from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeLanding,HomeAbout, HomeShows,HomeBlogs,Shows,Events,About,Contact,Staff

# Create your views here.
def home(request):
    homland = HomeLanding.get_homelanding()
    homabout = HomeAbout.get_homeabout()
    homshows = HomeShows.get_homeshows()
    homeblog = HomeBlogs.get_homeblogs()
    return render(request,'home.html', { "homland":homland , "homabout":homabout, "homshows":homshows, "homeblog":homeblog})

def shows(request):
    shows = Shows.get_allshows()
    return render(request, 'shows.html', { "shows":shows})

def about(request):
    about = About.get_aboutcontent()
    staff = Staff.get_staffinfo()
    return render(request, 'about.html', {"about":about , "staff":staff})

def blog(request):
    return render(request, 'blog.html')

def events(request):
    event = Events.get_allevents()
    return render(request, 'events.html', {"event":event})

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    contact = Contact.get_contacts()
    return render(request, 'contact.html', {"contact":contact})
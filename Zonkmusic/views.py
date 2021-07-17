from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeLanding,HomeAbout, HomeShows,HomeBlogs1,HomeBlogs2,HomeBlogs3,Shows,Events,About1,About2,About3,Contact,Staff,HomeGenre1,HomeGenre2

# Create your views here.
def home(request):
    homland = HomeLanding.get_homelanding()
    homabout = HomeAbout.get_homeabout()
    homshows = HomeShows.get_homeshows()
    homeblog1 = HomeBlogs1.get_homeblogs1()
    homeblog2 = HomeBlogs2.get_homeblogs2()
    homeblog3 = HomeBlogs3.get_homeblogs3()
    genre1 = HomeGenre1.get_genre()
    genres = HomeGenre2.get_allgenres()
    return render(request,'home.html', { "homland":homland , "homabout":homabout, "homshows":homshows, "homeblog1":homeblog1, "homeblog2":homeblog2, "homeblog3":homeblog3, "genre1":genre1, "genres":genres})

def shows(request):
    shows = Shows.get_allshows()
    return render(request, 'shows.html', { "shows":shows})

def about(request):
    about1 = About1.get_about1content()
    about2 = About2.get_about2content()
    about3 = About3.get_about3content()
    staffs = Staff.get_staffinfo()
    return render(request, 'about.html', {"about1":about1, "about2":about2, "about3":about3,"staffs":staffs})

def blog(request):
    return render(request, 'blog.html')

def events(request):
    events = Events.get_allevents()
    return render(request, 'events.html', {"events":events})

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    contact = Contact.get_contacts()
    return render(request, 'contact.html', {"contact":contact})
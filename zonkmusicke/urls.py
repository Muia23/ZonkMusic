from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.home,name ='home'),
    url(r'^shows$',views.shows,name ='shows'),
    url(r'^about$',views.about,name ='about'),
    url(r'^blog$',views.blog,name ='blog'),
    url(r'^contact$',views.contact,name ='contact'),
    url(r'^events$',views.events,name ='events'),
    url(r'^gallery$',views.gallery,name ='gallery'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
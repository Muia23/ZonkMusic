from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class HomeLanding(models.Model):
    landingbackground = models.FileField(upload_to = 'media')
    landinglogo = models.FileField(upload_to = 'images')
    landingheading = models.CharField(max_length=100)
    landingtext = models.TextField()

    @classmethod
    def get_homelanding(cls):
        homland = cls.objects.get(pk=1)
        return homland

class HomeAbout(models.Model):
    aboutimg = models.FileField(upload_to = 'media')
    abouttitle = models.CharField(max_length= 60)
    aboutpara1 = models.TextField()    
    aboutpara2 = models.TextField()    

    @classmethod
    def get_homeabout(cls):
        homabout = cls.objects.get(pk=1)
        return homabout


class HomeShows(models.Model):
    showdate = models.CharField(max_length= 60)
    showtitle = models.CharField(max_length=120)
    showhost = models.CharField(max_length= 60)
    eattime = models.CharField(max_length= 60)
    cattime = models.CharField(max_length= 60)

    @classmethod
    def get_homeshows(cls):
        homshow = cls.objects.all()
        return homshow

class HomeBlogs(models.Model):
    blogimg1 = models.FileField(upload_to = 'media')
    blogheading1 = models.CharField(max_length= 60)
    blogtext1 = models.CharField(max_length= 60)
    blogdate1 = models.CharField(max_length= 60)    
    blogimg2 = models.FileField(upload_to = 'media')
    blogheading2 = models.CharField(max_length= 60)
    blogtext2 = models.CharField(max_length= 60)
    blogdate2 = models.CharField(max_length= 60)    
    blogimg3 = models.FileField(upload_to = 'media')
    blogheading3 = models.CharField(max_length= 60)
    blogtext3 = models.CharField(max_length= 60)
    blogdate3 = models.CharField(max_length= 60)    

class Shows(models.Model):
    showimg1 = models.FileField(upload_to = 'media')
    showtitle1 = models.CharField(max_length= 60)
    showperiod1 = models.CharField(max_length= 60)  
    showtime1 = models.CharField(max_length= 60)  
    showabout1 = models.TextField()    
    showurl1 = models.URLField(max_length = 200)
    showimg2 = models.FileField(upload_to = 'media')
    showtitle2 = models.CharField(max_length= 60)
    showperiod2 = models.CharField(max_length= 60)  
    showtime2 = models.CharField(max_length= 60)  
    showabout2 = models.TextField()    
    showurl2 = models.URLField(max_length = 200)

    @classmethod
    def get_allshows(cls):
        allshows = cls.objects.all().order_by('-id')
        return allshows

class Events(models.Model):
    eventimg = models.FileField(upload_to = 'media')
    eventtxt = models.CharField(max_length= 60)  

class About(models.Model):
    abouttitle1 = models.CharField(max_length= 60)
    abouttext1 = models.TextField()    
    abouttitle2 = models.CharField(max_length= 60)
    abouttext2 = models.TextField()    
    abouttitle3 = models.CharField(max_length= 60)
    abouttext3 = models.TextField()    
    staffimg = models.FileField(upload_to = 'media')
    staffname = models.CharField(max_length= 60)
    stafftitle = models.CharField(max_length= 60)

class Contact(models.Model):
    contactbuilding = models.CharField(max_length= 60)
    contactcountry = models.CharField(max_length= 60)
    contactphone = models.CharField(max_length= 60)
    contactemail = models.CharField(max_length= 60)
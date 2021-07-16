from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class HomeLanding(models.Model):
    landingbackground = models.FileField(upload_to = 'media')
    landinglogo = models.FileField(upload_to = 'images')
    landingheading1 = models.CharField(max_length=100)
    landingtext1 = models.TextField()
    landingheading2 = models.CharField(max_length=100)
    landingtext2 = models.TextField()

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
        homshow = cls.objects.all().order_by('id')
        return homshow

class HomeBlogs(models.Model):
    blogimg1 = models.FileField(upload_to = 'media')
    blogheading1 = models.CharField(max_length= 60)
    blogtext1 = models.CharField(max_length= 60)
    blogdate1 = models.CharField(max_length= 60)  
    blogurl1 = models.URLField(max_length = 200)  
    blogimg2 = models.FileField(upload_to = 'media')
    blogheading2 = models.CharField(max_length= 60)
    blogtext2 = models.CharField(max_length= 60)
    blogdate2 = models.CharField(max_length= 60)   
    blogurl2 = models.URLField(max_length = 200)   
    blogimg3 = models.FileField(upload_to = 'media')
    blogheading3 = models.CharField(max_length= 60)
    blogtext3 = models.CharField(max_length= 60)
    blogdate3 = models.CharField(max_length= 60)
    blogurl3 = models.URLField(max_length = 200)  

    @classmethod
    def get_homeblogs(cls):
        homeblogs = cls.objects.get(pk=1)
        return homeblogs    

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
        allshows = cls.objects.all().order_by('id')
        return allshows

class Events(models.Model):
    eventimg1 = models.FileField(upload_to = 'media')
    eventtxt1 = models.CharField(max_length= 60)  
    eventimg2 = models.FileField(upload_to = 'media')
    eventtxt2 = models.CharField(max_length= 60)  
    eventimg3 = models.FileField(upload_to = 'media')
    eventtxt3 = models.CharField(max_length= 60)  

    @classmethod
    def get_allevents(cls):
        allevents = cls.objects.get(pk=1)
        return allevents

class About(models.Model):
    abouttitle1 = models.CharField(max_length= 60)
    abouttexta = models.TextField()    
    abouttextb = models.TextField()    
    abouttitle2 = models.CharField(max_length= 60)
    abouttextc = models.TextField()    
    abouttextd = models.TextField()    
    abouttitle3 = models.CharField(max_length= 60)
    abouttexte = models.TextField()    
    abouttextf = models.TextField()    
    abouttextg = models.TextField()

    @classmethod
    def get_aboutcontent(cls):
        about = cls.objects.get(pk=1)
        return about    

class Staff(models.Model):
    staffimg1 = models.FileField(upload_to = 'media')
    staffname1 = models.CharField(max_length= 60)
    stafftitle1 = models.CharField(max_length= 60)
    staffimg2 = models.FileField(upload_to = 'media')
    staffname2 = models.CharField(max_length= 60)
    stafftitle2 = models.CharField(max_length= 60)
    staffimg3 = models.FileField(upload_to = 'media')
    staffname3 = models.CharField(max_length= 60)
    stafftitle3 = models.CharField(max_length= 60)
    staffimg4 = models.FileField(upload_to = 'media')
    staffname4 = models.CharField(max_length= 60)
    stafftitle4 = models.CharField(max_length= 60)
    staffimg5 = models.FileField(upload_to = 'media')
    staffname5 = models.CharField(max_length= 60)
    stafftitle5 = models.CharField(max_length= 60)
    staffimg6 = models.FileField(upload_to = 'media')
    staffname6 = models.CharField(max_length= 60)
    stafftitle6 = models.CharField(max_length= 60)

    @classmethod
    def get_staffinfo(cls):
        staff = cls.objects.get(pk=1)
        return staff

class Contact(models.Model):
    contactbuilding = models.CharField(max_length= 60)
    contactcountry = models.CharField(max_length= 60)
    contactphone = models.CharField(max_length= 60)
    contactemail = models.CharField(max_length= 60)

    @classmethod
    def get_contacts(cls):
        contacts = cls.objects.get(pk=1)
        return contacts
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class HomeLanding(models.Model):
    landingbackground = models.FileField(upload_to = 'media/%y')
    landinglogo = models.ImageField(null=True, blank=True, upload_to="media/")
    landingheading1 = models.CharField(max_length=100)
    landingtext1 = models.TextField()
    landingheading2 = models.CharField(max_length=100)
    landingtext2 = models.TextField()    

    @classmethod
    def get_homelanding(cls):
        homland = cls.objects.all()
        return homland

class HomeGenre1(models.Model):
    genreimg = models.ImageField(null=True, blank=True, upload_to="media/")
    genretext = models.CharField(max_length=100)

    @classmethod
    def get_genre(cls):
        genre = cls.objects.all()
        return genre

class HomeGenre2(models.Model):
    genreimg = models.ImageField(null=True, blank=True, upload_to="media/")
    genretext = models.CharField(max_length=100)

    @classmethod
    def get_allgenres(cls):
        genres = cls.objects.all()
        return genres

class HomeAbout(models.Model):
    aboutimg = models.ImageField(null=True, blank=True, upload_to="media/")
    abouttitle = models.CharField(max_length= 60)
    aboutpara1 = models.TextField()    
    aboutpara2 = models.TextField()    

    @classmethod
    def get_homeabout(cls):
        homabout = cls.objects.all()
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

class HomeBlogs1(models.Model):
    blogimg = models.ImageField(null=True, blank=True, upload_to="media/")
    blogheading = models.CharField(max_length= 60)
    blogtext = models.CharField(max_length= 60)
    blogdate = models.CharField(max_length= 60)  
    blogurl = models.URLField(max_length = 200)  

    @classmethod
    def get_homeblogs1(cls):
        homeblogs = cls.objects.all()
        return homeblogs    

class HomeBlogs2(models.Model):
    blogimg = models.ImageField(null=True, blank=True, upload_to="media/")
    blogheading = models.CharField(max_length= 60)
    blogtext = models.CharField(max_length= 60)
    blogdate = models.CharField(max_length= 60)   
    blogurl = models.URLField(max_length = 200)  

    @classmethod
    def get_homeblogs2(cls):
        homeblogs = cls.objects.all()
        return homeblogs    

class HomeBlogs3(models.Model): 
    blogimg = models.ImageField(null=True, blank=True, upload_to="media/")
    blogheading = models.CharField(max_length= 60)
    blogtext = models.CharField(max_length= 60)
    blogdate = models.CharField(max_length= 60)
    blogurl = models.URLField(max_length = 200)  

    @classmethod
    def get_homeblogs3(cls):
        homeblogs = cls.objects.all()
        return homeblogs    

class Shows(models.Model):
    showimg = models.ImageField(null=True, blank=True, upload_to="media/")
    showtitle = models.CharField(max_length= 60)
    showperiod = models.CharField(max_length= 60)  
    showtime = models.CharField(max_length= 60)  
    showabout = models.TextField()    
    showurl = models.URLField(max_length = 200)    

    @classmethod
    def get_allshows(cls):
        allshows = cls.objects.all()
        return allshows

class Events(models.Model):
    eventimg = models.ImageField(null=True, blank=True, upload_to="media/")
    eventtxt = models.CharField(max_length= 60)      

    @classmethod
    def get_allevents(cls):
        allevents = cls.objects.all().order_by('id')
        return allevents

class About1(models.Model):
    abouttitle = models.CharField(max_length= 60)
    abouttexta = models.TextField()    
    abouttextb = models.TextField()  

    @classmethod
    def get_about1content(cls):
        about = cls.objects.get(pk=1)
        return about    
  
class About2(models.Model):
    abouttitle = models.CharField(max_length= 60)
    abouttexta = models.TextField()    
    abouttextb = models.TextField()    

    @classmethod
    def get_about2content(cls):
        about = cls.objects.get(pk=1)
        return about    

class About3(models.Model):
    abouttitle = models.CharField(max_length= 60)
    abouttexta = models.TextField()    
    abouttextb = models.TextField()    
    abouttextc = models.TextField()

    @classmethod
    def get_about3content(cls):
        about = cls.objects.get(pk=1)
        return about    

class Staff(models.Model):
    staffimg1 = models.ImageField(null=True, blank=True, upload_to="media/")
    staffname1 = models.CharField(max_length= 60)
    stafftitle1 = models.CharField(max_length= 60)    

    @classmethod
    def get_staffinfo(cls):
        staff = cls.objects.all()
        return staff

class Contact(models.Model):
    contactbuilding = models.CharField(max_length= 60)
    contactcountry = models.CharField(max_length= 60)
    contactphone = models.CharField(max_length= 60)
    contactemail = models.CharField(max_length= 60)

    @classmethod
    def get_contacts(cls):
        contacts = cls.objects.get(pk=2)
        return contacts
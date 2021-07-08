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

    
    
    
from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100, blank=True)
    paragraph = models.CharField(max_length=300, blank=True)
    # store an image
    image = models.ImageField(upload_to='images/', blank=True)
    mainpara = models.CharField(max_length=300, blank=True)
    maintitle = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.title

class Services(models.Model):
    serviceimage = models.ImageField(upload_to="images/",blank= True )
    servicetitle =  models.CharField ( max_length=40 , blank=True)
    serviceparagraphtwo =   models.TextField()
    def __str__ ( self ):
        return self.servicetitle

class About(models.Model):
    title = models.TextField()
    aboutimage = models.ImageField( upload_to ="images/" , blank=True)
    aboutpara = models.TextField()

    def __str__ ( self ):
        return self.title


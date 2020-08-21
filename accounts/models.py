from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.



class Musician(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, default="nayak" , null=True)
    profile_pic = models.ImageField(default= 'profile1.png' ,null=True, blank=True)
    instrument = models.CharField(max_length=100, null=True, default="guitar")
    
    def __str__(self):
        return self.first_name


class Seasons(models.Model):
    CHOICES = (
        ('Winter','Winter'),
        ('Summer','Summer'),
        ('Spring','Spring'),
        ('Rainy', 'Rainy'),
    )

    choice = models.CharField(max_length=10, choices=CHOICES , null=True)

    def __str__(self):
        return self.choice
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    season = models.ManyToManyField(Seasons, blank=True)
    release_date = models.DateField(blank=True, null=True, auto_now_add=timezone.now())
    num_stars = models.IntegerField(null=True, default=1 )

    def __str__(self):
        return self.name

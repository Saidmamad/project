from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

class Tour(models.Model):
    TourOperator = models.ForeignKey(TourOperator, on_delete=models.PROTECT)
    TourCode = models.CharField(max_length=10, unique=True, help_text='Ex. JT001 ') #user = models.OneToOneField(User)
    Title = models.CharField(max_length=200, help_text="Title of the tour here")
    Slug = models.SlugField(max_length=200)
    Type = models.CharField(max_length=200, choices = TOUR_TYPES, help_text="Select from the list")
    Duration = models.IntegerField(default=0)
    ShortDesc = models.CharField(max_length=200, help_text='Short description in 200')
    Description = models.TextField(help_text='Description of the tour...')
    Itinerary = models.CharField(max_length=500, help_text="Itinerary of the tour...")
    Inclusions = models.CharField(max_length=200, help_text="Inclusions of the tour; Seperate them with commas")
    Exclusions = models.CharField(max_length=200, help_text="Exclusions of the tour; Seperate them with commas")
    Difficulty = models.CharField(max_length=20, help_text="Enter a value between 1 to 10")
    GroupSize = models.CharField(max_length=2, help_text="Group size")
    Seasonality = models.CharField(max_length=100, help_text="Seasonality of the tour; Ex. July - September")
    Highlights = models.CharField(max_length=100, help_text="Highlights of the tour; Ex. Yamchun fortress, etc")
    #Destination_id = models.ForeignKey(Destination)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Image = models.ImageField(upload_to='tours_image/')
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Available = models.BooleanField(default=True)
    Rating = models.IntegerField()
    StartDate = models.DateField(auto_now=True)
    EndDate = models.DateField(auto_now=True)

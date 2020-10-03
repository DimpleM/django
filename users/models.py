from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
from django.utils.html import mark_safe
import os
class Address(models.Model):
    street = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    pincode = models.CharField(max_length=100,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return "From {}, to {}".format(self.city, self.country)


class Profile(models.Model):
    GENDER_CHOICES = (
        (u'Male', u'Male'),
        (u'Female', u'Female'),
        (u'Other', u'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,blank= True,null=True)
    image = models.ImageField(upload_to='', blank=True)
    DateOfBirth = models.DateField(blank= True,null=True) 
    perAddress = models.OneToOneField(Address, on_delete=models.SET_NULL, related_name='perAddress',  null=True)
    comAddress = models.OneToOneField(Address, on_delete=models.SET_NULL, related_name='comAddresss', null=True)
    friends = models.ManyToManyField("Profile", blank=True)
    def url(self):
            return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    def __str__(self):
        return self.user.username
          



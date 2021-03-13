from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime,time
from django import forms
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length = 200)
    loc_type = models.CharField(max_length = 100)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    location_found = models.ForeignKey(Location, null = True, on_delete = models.CASCADE)
    description = models.CharField(max_length = 300)
    tags = models.CharField(max_length = 200)
    time = models.TimeField( default=timezone.now(), blank=True)
    date = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return name
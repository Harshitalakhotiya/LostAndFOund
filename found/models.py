from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length = 200)
    loc_type = models.CharField(max_length = 100)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    location_found = models.ForeignKey(Location, null = True, on_delete = models.CASCADE)
    description = models.CharField(max_length = 300)
    tags = models.CharField(max_length = 200)

    time_found = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime,time
from django import forms
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    tags = models.CharField(max_length = 200)
    time = models.TimeField( default=timezone.now(), blank=True)
    date = models.DateField(default=datetime.now(), blank=True)
    person = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)


    def __str__(self):
        return self.name
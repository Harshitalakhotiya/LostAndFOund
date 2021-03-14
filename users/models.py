from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime,time
from django import forms
from django.utils import timezone
from found.models import *


class meetup(models.Model):
    lost_end = models.IntegerField()
    found_end = models.IntegerField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE,null=True)
    isLost = models.BooleanField(default = False)


    # def __str__(self):
    #     return self.name

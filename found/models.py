from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
	name = models.CharField(max_length = 200)

class Stations(Location):
	pass

class BusStop(Location):
	pass

class Product(models.Model):
	name = models.CharField(max_length = 200)

class Item(models.Model):
	name = models.CharField(max_length = 200)

class Tags(models.Model):
	name = models.CharField(max_length = 100)
    prod_id = models.ForeignKey(Product, null = True, on_delete = models.CASCADE)
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class University(models.Model):
    name = models.CharField(max_length=500)


class Event(models.Model):
    name = models.CharField(max_length=500)
    time = models.DateTimeField()
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)

    universities = models.ManyToManyField(University)


class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=10000)


class Transaction(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    date_of_sale = models.DateTimeField()
    price = models.FloatField()
    quantity = models.IntegerField()

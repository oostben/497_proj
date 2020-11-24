from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class University(models.Model):
    name = models.CharField(max_length=500)
    domain_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    venmo = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField()
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    cover = models.ImageField(upload_to='images/', null=True)

    universities = models.ManyToManyField(University)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=10000)


class Transaction(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    date_of_sale = models.DateTimeField()
    price = models.FloatField()
    quantity = models.IntegerField()


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="receiver", on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=10000)

    @classmethod
    def for_user(cls, user):
        as_sender = cls.objects.filter(sender=user)
        as_receiver = cls.objects.filter(receiver=user)

        result = [m for m in as_sender]
        result.extend([m for m in as_receiver])

        return result

    def __str__(self):
        return f"{self.pub_date}: {self.message}"

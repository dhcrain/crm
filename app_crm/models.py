from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Asset(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    email = models.EmailField()
    website = models.CharField(max_length=300)
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=4)
    country = models.CharField(max_length=30)

class User(models.Model):
    asset = models.ForeignKey(Asset)
    user = models.ForeignKey("auth.User")

class Company(models.Model):
    users = models.ForeignKey("auth.User")
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    website = models.CharField(max_length=300)
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=4)
    country = models.CharField(max_length=30)

class Customer(models.Model):
    asset = models.ForeignKey(Asset)
    notes = models.TextField(null=True, blank=True)
    # Other fields can be applied here... just need to flesh out this functionality
    # What things do you need to know about a customer that are not in the company level or the asset level?

class Orginization(models.Model):
    customers = models.ForeignKey(Customer)
    # Also not completely sure of full functionality here.

class Note(models.Model):
    users = models.ForeignKey("auth.User")

class Task(models.Model):
    users = models.ForeignKey("auth.User")

class Tag(models.Model):
    users = models.ForeignKey("auth.User")

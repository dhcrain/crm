from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    name = models.CharField(max_length=50)


class Asset(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=True)
    is_company = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
    email = models.EmailField()
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=4)
    zip_code = models.IntegerField(max_length=10)
    country = models.CharField(max_length=30)
    website = models.URLField(max_length=350)
    twitter = models.URLField(max_length=350)
    facebook = models.URLField(max_length=350)
    linkedin = models.URLField(max_length=350)
    profile_picture = models.ImageField(upload_to="profile_images", blank=True, null=True)


class Note(models.Model):
    note_creator = models.ForeignKey('auth.User')
    note_is_about = models.ForeignKey(Asset)
    note = models.TextField()
    note_picture = models.ImageField(upload_to="note_images", blank=True, null=True)
    note_file = models.FileField(upload_to='note_files', blank=True, null=True)
    created = models.DateTimeField(auto_now=True)


class Task(models.Model):
    creator = models.ForeignKey('auth.User')
    assigned_to = models.ForeignKey('auth.User')  # ?
    task_is_about = models.ForeignKey(Asset)
    task = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    user = models.ManyToManyField('auth.User')
    tag = models.CharField(max_length=25)


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Asset.objects.create(profile_user=instance)

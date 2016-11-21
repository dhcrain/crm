from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from localflavor.us.models import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Asset(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=True)
    is_company = models.BooleanField(default=False, verbose_name='Is This a Company?')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneNumberField(blank=True) # https://django-localflavor.readthedocs.io/en/latest/localflavor/us/
    email = models.EmailField(blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    street2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=4, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField(max_length=350, blank=True, null=True)
    twitter = models.URLField(max_length=350, blank=True, null=True)
    facebook = models.URLField(max_length=350, blank=True, null=True)
    linkedin = models.URLField(max_length=350, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_images", blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    @property
    def profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return "http://www.sessionlogs.com/media/icons/defaultIcon.png"


class Note(models.Model):
    note_creator = models.ForeignKey('auth.User', null=True, blank=True)
    note_is_about = models.ForeignKey(Asset)
    note = models.TextField()
    note_picture = models.ImageField(upload_to="note_images", blank=True, null=True)
    note_file = models.FileField(upload_to='note_files', blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}, {}'.format(self.note_creator, self.note_is_about)

class Task(models.Model):
    creator = models.ForeignKey('auth.User', null=True, blank=True)
    assigned_to = models.ForeignKey('auth.User', related_name="Assignee")
    task_is_about = models.ForeignKey(Asset)
    task = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    user = models.ManyToManyField('auth.User')
    tag = models.CharField(max_length=25)

    def __str__(self):
        return self.tag

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Asset.objects.create(user=instance)

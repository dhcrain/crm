# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company', models.BooleanField(default=False, verbose_name='Is This a Company?')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', localflavor.us.models.PhoneNumberField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('street2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=4)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('website', models.URLField(blank=True, max_length=350, null=True)),
                ('twitter', models.URLField(blank=True, max_length=350, null=True)),
                ('facebook', models.URLField(blank=True, max_length=350, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=350, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('note_picture', models.ImageField(blank=True, upload_to='note_images')),
                ('note_file', models.FileField(blank=True, upload_to='note_files')),
                ('created', models.DateTimeField(auto_now=True)),
                ('note_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('note_is_about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignee', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task_is_about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.Asset')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_crm.Company'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app_crm.Tag'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

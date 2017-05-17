# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-17 07:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('chatroomAdmin', models.ManyToManyField(related_name='chatroomAdmin', to=settings.AUTH_USER_MODEL)),
                ('chatroomUsers', models.ManyToManyField(related_name='chatroomUsers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=500)),
                ('message_picture', models.CharField(max_length=5000)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pichature.Chatroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
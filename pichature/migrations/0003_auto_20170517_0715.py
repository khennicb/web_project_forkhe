# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-17 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pichature', '0002_auto_20170517_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_picture',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erm_automation', '0002_event_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventreference',
            name='event_value',
        ),
    ]
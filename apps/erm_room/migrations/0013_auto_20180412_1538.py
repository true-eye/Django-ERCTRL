# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-12 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0012_auto_20180319_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liveviewfont',
            options={'ordering': ('id',), 'verbose_name': 'Live View Font', 'verbose_name_plural': 'Live View Fonts'},
        ),
    ]

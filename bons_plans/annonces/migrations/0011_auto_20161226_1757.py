# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-26 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0010_auto_20161226_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-27 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0011_auto_20161226_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-30 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0005_auto_20171130_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0014_auto_20171214_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(default=(2017, 12, 14)),
            preserve_default=False,
        ),
    ]

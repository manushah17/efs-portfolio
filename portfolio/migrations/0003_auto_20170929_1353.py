# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-29 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170929_1239'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('name', 'email')]),
        ),
    ]

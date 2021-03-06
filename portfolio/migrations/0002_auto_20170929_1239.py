# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-29 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('cust_number', 'name', 'cell_phone')]),
        ),
    ]

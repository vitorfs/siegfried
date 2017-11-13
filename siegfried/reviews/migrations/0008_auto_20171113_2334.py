# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20171113_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'illness length'), (2, 'follow-up period'), (3, 'spectrum of disease')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='criteria',
            name='operator',
            field=models.PositiveSmallIntegerField(choices=[(1, 'greater than'), (2, 'less than'), (3, 'in'), (5, 'equal to')], default=1),
            preserve_default=False,
        ),
    ]
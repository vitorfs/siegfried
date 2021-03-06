# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20171113_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'illness length'), (2, 'follow-up period'), (3, 'spectrum of disease'), (4, 'type of study'), (5, 'diagnosis system')]),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]

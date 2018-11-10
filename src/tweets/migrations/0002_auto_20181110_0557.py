# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-10 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
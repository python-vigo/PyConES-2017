# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0006_speaker_presentation_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='presentation_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]

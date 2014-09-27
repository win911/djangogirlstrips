# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title2',
            field=models.CharField(default=datetime.date(2014, 9, 27), max_length=100),
            preserve_default=False,
        ),
    ]

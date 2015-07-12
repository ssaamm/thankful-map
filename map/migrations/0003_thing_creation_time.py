# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150712_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 21, 35, 26, 406752, tzinfo=utc)),
        ),
    ]

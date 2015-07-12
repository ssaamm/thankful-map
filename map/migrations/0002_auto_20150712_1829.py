# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='location',
        ),
        migrations.AddField(
            model_name='thing',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thing',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=7),
            preserve_default=False,
        ),
    ]

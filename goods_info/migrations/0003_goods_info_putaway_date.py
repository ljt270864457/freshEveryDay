# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('goods_info', '0002_auto_20161101_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_info',
            name='putaway_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 1, 19, 3, 59, 961280), auto_now=True),
            preserve_default=False,
        ),
    ]

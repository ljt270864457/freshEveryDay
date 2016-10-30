# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recent_views',
            name='view_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

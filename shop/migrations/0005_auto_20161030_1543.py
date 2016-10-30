# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20161030_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_info',
            name='unit',
            field=models.CharField(default=b'500g', max_length=20),
        ),
    ]

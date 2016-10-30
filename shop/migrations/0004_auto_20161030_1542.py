# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_info',
            name='unit',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_info',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order_record',
            options={'managed': False},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='deli_address',
            table='deli_address',
        ),
        migrations.AlterModelTable(
            name='goods_cate',
            table='goods_cate',
        ),
        migrations.AlterModelTable(
            name='goods_info',
            table='goods_info',
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.AlterModelTable(
            name='order_record',
            table='order_record',
        ),
        migrations.AlterModelTable(
            name='recent_views',
            table='recent_views',
        ),
        migrations.AlterModelTable(
            name='user_info',
            table='user_info',
        ),
    ]

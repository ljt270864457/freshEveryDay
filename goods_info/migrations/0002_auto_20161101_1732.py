# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_cate',
            name='img_url',
            field=models.ImageField(upload_to=b'upload/'),
        ),
        migrations.AlterField(
            model_name='goods_info',
            name='img_url',
            field=models.ImageField(upload_to=b'upload/'),
        ),
    ]

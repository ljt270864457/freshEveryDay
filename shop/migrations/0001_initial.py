# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buy_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='deli_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deli_name', models.CharField(max_length=50)),
                ('detail_address', models.TextField()),
                ('postcode', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='goods_cate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('img_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='goods_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('desc', models.TextField()),
                ('cate_id', models.ForeignKey(to='shop.goods_cate')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=20)),
                ('order_time', models.DateTimeField()),
                ('is_pay', models.BooleanField()),
                ('total_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('deli_id', models.ForeignKey(to='shop.deli_address')),
            ],
        ),
        migrations.CreateModel(
            name='order_record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_count', models.IntegerField()),
                ('goods_id', models.ForeignKey(to='shop.goods_info')),
                ('order_id', models.ForeignKey(to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='recent_views',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_time', models.DateTimeField()),
                ('goods_id', models.ForeignKey(to='shop.goods_info')),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('registe_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='recent_views',
            name='user_id',
            field=models.ForeignKey(to='shop.user_info'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(to='shop.user_info'),
        ),
        migrations.AddField(
            model_name='deli_address',
            name='user_id',
            field=models.ForeignKey(to='shop.user_info'),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods_id',
            field=models.ForeignKey(to='shop.goods_info'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(to='shop.user_info'),
        ),
    ]

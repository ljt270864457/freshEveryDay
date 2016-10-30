# -*- coding=utf-8 -*-
from django.db import models

# 用户信息表
class user_info(models.Model):
	name = models.CharField(max_length=50)
	passwd = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=11,null=True,blank=True)
	registe_date = models.DateTimeField(auto_now=True)
	address = models.CharField(max_length=100)

	class Meta():
		db_table = 'user_info'

# 商品分类表
class goods_cate(models.Model):
	name = models.CharField(max_length=100)
	img_url = models.TextField()

	class Meta():
		db_table = 'goods_cate'

# 商品信息表
class goods_info(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	cate_id = models.ForeignKey('goods_cate')
	stock = models.IntegerField()
	img_url = models.CharField(max_length=200)
	intro = models.TextField()
	desc = models.TextField()
	unit = models.CharField(max_length=20)

	class Meta():
		db_table = 'goods_info'

# 最近浏览表
class recent_views(models.Model):
	goods_id = models.ForeignKey('goods_info')
	user_id = models.ForeignKey('user_info')
	view_time = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'recent_views'

# 订单基本信息表
class order(models.Model):
	user_id = models.ForeignKey('user_info')
	order_time = models.DateTimeField(auto_now=True)
	is_pay = models.BooleanField()
	deli_id = models.ForeignKey('deli_address')
	total_price = models.DecimalField(max_digits=10,decimal_places=2)

	class Meta():
		db_table = 'order'

# 订单详细信息表
class order_record(models.Model):
	order_id = models.ForeignKey('order')
	goods_id = models.ForeignKey('goods_info')
	goods_count = models.IntegerField()

	class Meta():
		db_table = 'order_record'

# 收货地址表
class deli_address(models.Model):
	user_id = models.ForeignKey('user_info')
	deli_name = models.CharField(max_length=50)
	detail_address = models.TextField()
	postcode = models.CharField(max_length=6)
	phone_number = models.CharField(max_length=11)

	class Meta():
		db_table = 'deli_address' 

# 购物车表
class cart(models.Model):
	user_id = models.ForeignKey('user_info')
	goods_id = models.ForeignKey('goods_info')
	buy_count = models.IntegerField()

	class Meta():
		db_table = 'cart'
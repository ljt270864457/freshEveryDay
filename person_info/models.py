# coding=utf-8
from django.db import models

# 最近浏览表
class recent_views(models.Model):
	goods_id = models.ForeignKey('goods_info.goods_info')
	user_id = models.ForeignKey('login.user_info')
	view_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.pk

	class Meta():
		db_table = 'recent_views'

# 订单基本信息表
class order(models.Model):
	user_id = models.ForeignKey('login.user_info')
	order_time = models.DateTimeField(auto_now=True)
	is_pay = models.BooleanField()
	deli_id = models.ForeignKey('deli_address')
	total_price = models.DecimalField(max_digits=10,decimal_places=2)

	def __unicode__(self):
		return self.pk

	class Meta():
		db_table = 'order'

# 订单详细信息表
class order_record(models.Model):
	order_id = models.ForeignKey('order')
	goods_id = models.ForeignKey('goods_info.goods_info')
	goods_count = models.IntegerField()
	
	def __unicode__(self):
		return self.pk

	class Meta():
		db_table = 'order_record'

# 收货地址表
class deli_address(models.Model):
	user_id = models.ForeignKey('login.user_info')
	deli_name = models.CharField(max_length=50)
	detail_address = models.TextField()
	postcode = models.CharField(max_length=6)
	phone_number = models.CharField(max_length=11)

	def __unicode__(self):
		return self.pk

	class Meta():
		db_table = 'deli_address' 

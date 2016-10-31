# encoding=utf-8
from django.db import models

# 购物车表
class cart(models.Model):
	user_id = models.ForeignKey('login.user_info')
	goods_id = models.ForeignKey('goods_info.goods_info')
	buy_count = models.IntegerField()

	def __unicode__(self):
		return self.pk

	class Meta():
		db_table = 'cart'

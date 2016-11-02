# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# 商品分类表
class goods_cate(models.Model):
	name = models.CharField(max_length=100)
	img_url = models.ImageField(upload_to='upload/')

	def __unicode__(self):
		return self.name

	class Meta():
		db_table = 'goods_cate'

# 商品信息表
class goods_info(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	cate_id = models.ForeignKey('goods_info.goods_cate')
	stock = models.IntegerField()
	img_url = models.ImageField(upload_to='upload/')
	intro = models.TextField()
	desc = HTMLField()
	unit = models.CharField(max_length=20)
	sales_num = models.IntegerField(default=0)
	putaway_date = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.name

	class Meta():
		db_table = 'goods_info'
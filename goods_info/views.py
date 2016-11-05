#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from login import decrotors
from goods_info.models import *


# 需要查询的数据  
# 1.商品分类 2.商品名称、价格、图片url
@decrotors.login
def index(request,dic):
    cates = goods_cate.objects.all()
    dic['cates']=cates
    return render(request,'goods_info/index.html',dic)

@decrotors.login
def goodsType(request,dic):
	return render(request,'goods_info/list.html',dic)

@decrotors.login
def detail(request,dic):
	return render(request,'goods_info/detail.html',dic)



        

    








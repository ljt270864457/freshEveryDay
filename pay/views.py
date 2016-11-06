# coding=utf-8

from django.core.urlresolvers import reverse 
from django.shortcuts import render,redirect
from login import decrotors
from pay.models import *
from goods_info.models import *
from login.models import user_info
from django.http import HttpResponse,JsonResponse
import json

@decrotors.login
def myCart(request,dic):
	goodsList = []
	# 商品合计总价
	allGoodsPrice = 0
	userID = user_info.objects.get(name=dic['userName']).pk
	cartGoods = cart.objects.filter(user_id_id=userID)
	goodsCount = cart.objects.filter(user_id_id=userID).count()
	for good in cartGoods:
		goodID = good.goods_id_id
		goodInfo = goods_info.objects.get(pk=goodID)
		goodsList.append(goodInfo)	
	goodsList = list(set(goodsList))
	for goods in goodsList:
		sumPrice = goods.getSumPrice()
		allGoodsPrice+=sumPrice
	dic['goodsList'] = goodsList
	dic['goodsCount'] = goodsCount
	dic['allGoodsPrice'] = allGoodsPrice
	return render(request,'pay/cart.html',dic)

def delGoodsHandeler(request):
	if request.method =='POST':
		goodsID = int(request.POST['goodsID'])
		print goodsID
		cart2 = cart.objects.get(goods_id_id=goodsID)
		cart2.delete()
		flag=json.dumps({'isDelete':1})
		return jsonResponse(json.dumps(flag))


@decrotors.login
def placeOrder(request,dic):
	return render(request,'pay/place_order.html',dic)   


def filterDataHandeler(request):
	if request.method =='POST':
		AllID = request.POST['goodsID[]']
		print(AllID)
		if len(AllID)>0:
			for ID in AllID:
				goods = cart.objects.get(goods_id_id=int(ID))
				goods.delete()

	

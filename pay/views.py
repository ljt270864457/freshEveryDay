# coding=utf-8
from django.shortcuts import render
from login import decrotors
from pay.models import *
from goods_info.models import *
from django.http import HttpResponse,JsonResponse
import json

@decrotors.login
def myCart(request,dic):
	goodsList = []
	cartGoods = cart.objects.all()
	for good in cartGoods:
		goodID = good.goods_id_id
		goodInfo = goods_info.objects.get(pk=goodID)
		goodsList.append(goodInfo)	
	goodsList = list(set(goodsList))
	dic['goodsList'] = goodsList
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

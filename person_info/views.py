# coding = utf-8
from django.core.urlresolvers import reverse   
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from login.models import user_info
from goods_info.models import goods_info
from models import recent_views,deli_address
from pay.models import cart


def userInfo(request):
	goodsList = []
	goods_detail = []
	userInfo = user_info.objects.get(name='ljt')
	id = userInfo.pk
	name = userInfo.name
	telephone = userInfo.phone_number
	address = userInfo.address
	json_info = {'name':name,'phone_number':telephone,'address':address}
	recent_list = recent_views.objects.order_by('-view_time').all().filter(user_id = id)[:5]
	for goods in recent_list:
		goods_id = goods.goods_id_id		
		goodsList.append(goods_id)
 	for i in goodsList:
 		goods = goods_info.objects.get(id=i)
 		name = goods.name
		img_url = goods.img_url
		price = goods.price
		unit = goods.unit
		goods_detail.append({'name':name,'img_url':img_url,'price':price,'unit':unit})
	return render(request,'person_info/user_center_info.html',{'user_info':json_info,'goods_detail':goods_detail})

def userOrder(request):
	return render(request,'person_info/user_center_order.html')

def userSite(request):
	return render(request,'person_info/user_center_site.html')

def addressAddHandler(request):
	if request.method == 'POST':
		name = request.POST['name']
		address = request.POST['address']
		postcode = request.POST['postcode']
		phone_number = request.POST['phone_number']
		new_phone_num = formatPhoneNumber(phone_number)
		info = [name,address,postcode,new_phone_num]
	address = deli_address(user_id_id=1,deli_name=name,detail_address=address,postcode=postcode,phone_number=phone_number)
	address.save()
	return render(request,'person_info/user_center_site.html',{'info':info})

def addGoodsHanderler(request):
	if request.method == 'POST':
		name = request.POST['name']
	goods = goods_info.objects.get(name=name)
	goods_id = goods.pk
	user = user_info.objects.get(name = 'ljt')
	user_id = user.pk	
	count = 1
	json_info = {'userid':user_id,'goodsid':goods_id,'Buy_count':count}
	cart_info = cart(buy_count=count,goods_id_id=goods_id,user_id_id=user_id)
	cart_info.save()
	return JsonResponse(json_info)



def formatPhoneNumber(phone):
	return phone[0:3] + '*'*4 + phone[7:11]

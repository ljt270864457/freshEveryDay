#coding=utf-8

from django.core.urlresolvers import reverse   
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from login.models import user_info
from goods_info.models import goods_info
from models import *
from pay.models import cart
from toolKit import formatPhoneNumber

# 用户中心-个人信息视图函数
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

# 用户中心-个人信息视图函数
# 需要查询的数据：
# 下单时间、订单号、支付状态、商品名称、商品价格、单位、图片url、购买数量
def userOrder(request):
	orderList = orders.objects.filter(user_id_id=1).order_by('-order_time')[:2]	
	orderCount = orders.objects.filter(user_id_id=1).count() # 3

	# 某用户的订单号的集合
	orderIDList = [] # 4,3
	for i in orderList:
		orderIDList.append(i.pk)

	# 某用户每个订单的信息
	orderInfo = []

	# 订单中的商品信息
	goodsInfoList = [] # [{'goodsURL': <ImageFieldFile: upload/goods006.jpg>, 'goodsName': u'\u8fdb\u53e3\u897f\u6885', 'goodsPrice': Decimal('28.80'), 'goodsUnit': u'500g'}, {'goodsURL': <ImageFieldFile: upload/goods005.jpg>, 'goodsName': u'\u9ec4\u8089\u6843', 'goodsPrice': Decimal('10.00'), 'goodsUnit': u'500g'}]

	# 获取订单号及相应的信息
	# [{'isPay': False,'orderID': 4L,'orderTime': datetime.datetime(2016, 11, 1, 23, 5, 51, 141597)},

	 # {'isPay': True,'orderID': 3L,'orderTime': datetime.datetime(2016, 11, 1, 23, 5, 26, 375013)}]
	for orderID in orderIDList:
		order = orders.objects.get(pk=orderID)
		isPay = order.is_pay
		orderTime = order.order_time
		orderItem = {'orderID':orderID,'isPay':isPay,'orderTime':orderTime}
		orderInfo.append(orderItem)


	# 获取商品信息
	'''
		 {'goodsCount': 5L,
	  'goodsName': u'\u5410\u9c81\u756a\u68a8\u5149\u674f',
	  'goodsPrice': Decimal('5.50'),
	  'goodsURL': <ImageFieldFile: upload/goods004.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 4L},
	 {'goodsCount': 2L,
	  'goodsName': u'\u9999\u68a8',
	  'goodsPrice': Decimal('6.45'),
	  'goodsURL': <ImageFieldFile: upload/goods007.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 4L},
	 {'goodsCount': 1L,
	  'goodsName': u'\u6817\u5b50',
	  'goodsPrice': Decimal('9.50'),
	  'goodsURL': <ImageFieldFile: upload/goods008.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 4L},
	 {'goodsCount': 3L,
	  'goodsName': u'\u5927\u5174\u5927\u68da\u8349\u8393',
	  'goodsPrice': Decimal('16.80'),
	  'goodsURL': <ImageFieldFile: upload/goods003.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 3L},
	 {'goodsCount': 2L,
	  'goodsName': u'\u9ec4\u8089\u6843',
	  'goodsPrice': Decimal('10.00'),
	  'goodsURL': <ImageFieldFile: upload/goods005.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 3L},
	 {'goodsCount': 2L,
	  'goodsName': u'\u8fdb\u53e3\u897f\u6885',
	  'goodsPrice': Decimal('28.80'),
	  'goodsURL': <ImageFieldFile: upload/goods006.jpg>,
	  'goodsUnit': u'500g',
	  'orderID': 3L}]


	   '''

	for orderID in orderIDList:
		# 获取一个订单中的所有商品id
		goodsID = order_record.objects.filter(order_id_id=orderID)
		for num in goodsID:
			goodsInfo = goods_info.objects.get(pk=num.pk)	
			goodsName = goodsInfo.name
			goodsPrice = goodsInfo.price
			goodsUnit = goodsInfo.unit
			goodsURL = goodsInfo.img_url
			goodsCount = order_record.objects.filter(order_id_id=orderID).filter(goods_id_id=num.goods_id_id)
			goodsItem = {'orderID':orderID,'goodsName':goodsName,'goodsPrice':goodsPrice,'goodsUnit':goodsUnit,'goodsURL':goodsURL,'goodsCount':goodsCount[0].goods_count}
			goodsInfoList.append(goodsItem)

	return render(request,'person_info/user_center_order.html',{'orderInfo':orderInfo,'goodsInfoList':goodsInfoList})


# 用户中心-收货地址视图函数
def userSite(request):	
	reli_name = request.session.get('name')
	address = request.session.get('address')
	number = request.session.get('phone_number')
	if reli_name and address and address:
		json_info = {'address':address,'name':reli_name,'phone_number':number}
	else:
		address_list = deli_address.objects.filter(user_id_id=1).all().order_by('-id')
		address = address_list[0].detail_address
		reli_name = address_list[0].deli_name
		number = formatPhoneNumber(address_list[0].phone_number)
		json_info = {'address':address,'name':reli_name,'phone_number':number}
	return render(request,'person_info/user_center_site.html',{'json_info':json_info})

# 增加收货地址
# 如果能在session中能查到数据，那么从session中获取数据，否则查数据库中的最后一条
def addressAddHandler(request):
	if request.method == 'POST':
		name = request.POST['name']
		address = request.POST['address']
		postcode = request.POST['postcode']
		phone_number = request.POST['phone_number']
		new_phone_num = formatPhoneNumber(phone_number)
		info = [name,address,postcode,new_phone_num]
	address_info = deli_address(user_id_id=1,deli_name=name,detail_address=address,postcode=postcode,phone_number=phone_number)
	address_info.save()
	request.session['name']=name
	request.session['address']=address
	request.session['phone_number']=phone_number
	request.session.set_expiry(0)
	return redirect(reverse('freshEveryDay:userSite'))

# 购物车增加商品
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




from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *

def index(request):
	return render(request,'shop/index.html')

def user_center_info(request):
	userInfo = user_info.objects.get(pk=1)
	name = userInfo.name
	telephone = userInfo.phone_number
	address = userInfo.address
	json_info = {'name':name,'phone_number':telephone,'address':address}
	return render(request,'shop/user_center_info.html',{'user_info':json_info})

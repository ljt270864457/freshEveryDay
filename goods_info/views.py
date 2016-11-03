from django.shortcuts import render
from django.http import HttpResponse
from login import decrotors

@decrotors.login
def index(request,dic):
	return render(request,'goods_info/index.html',dic) 
	# return HttpResponse(dic['userName'])




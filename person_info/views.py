from django.shortcuts import render
from login.models import user_info

def userInfo(request):
	userInfo = user_info.objects.get(pk=1)
	name = userInfo.name
	telephone = userInfo.phone_number
	address = userInfo.address
	json_info = {'name':name,'phone_number':telephone,'address':address}
	return render(request,'person_info/user_center_info.html',{'user_info':json_info})

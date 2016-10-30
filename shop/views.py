from django.shortcuts import render
from models import *

def index(request):
	return render(request,'shop/user_center_site.html')

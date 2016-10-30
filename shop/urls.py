from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$',index,name = 'index'),
    url(r'^user_center_info/$',user_center_info,name ='user_center_info'),
]

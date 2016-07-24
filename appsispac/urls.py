from django.conf.urls import include, url
from appsispac.views import *

urlpatterns = [
	 url(r'^$',home,name='home'),
	 url(r'^frequencias/list$',frequencias_list,name='frequencias_list'),
	  url(r'^frequencias/update/(?P<pk>\d+)$',frequencias_update,name='frequencias_update'),
]

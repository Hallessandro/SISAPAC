from django.conf.urls import include, url
from appsispac.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^funcionario/list$',funcionario_list,name='funcionario_list'),
]

from django.conf.urls import include, url
from appsispac.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^funcionario/list$',funcionario_list,name='funcionario_list'),

	#Rotas de professores
	url(r'^professor/list$', professor_list, name='professor_list'),
]

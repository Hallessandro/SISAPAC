from django.conf.urls import include, url
from appsispac.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^funcionario/list$',funcionario_list,name='funcionario_list'),

	#Rotas de professores
	url(r'^professor/list$', professor_list, name='professor_list'),
	url(r'^professor/detail/(?P<pk>\d+)$', professor_detail, name='professor_detail'),
	url(r'^professor/update/(?P<pk>\d+)$', professor_update, name='professor_update'),
	url(r'^professor/new/$', professor_new, name='professor_new'),

	url(r'^horario/professor/new/$', horario_professor_new, name='horario_professor_new'),
]

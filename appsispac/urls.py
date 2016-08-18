from django.conf.urls import include, url
from appsispac.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^funcionario/list$',funcionario_list,name='funcionario_list'),

	#Rotas de funcionarios
	url(r'^funcionario/list$', funcionario_list, name='funcionario_list'),
	url(r'^funcionario/detail/(?P<pk>\d+)$', funcionario_detail, name='funcionario_detail'),
	url(r'^funcionario/update/(?P<pk>\d+)$', funcionario_update, name='funcionario_update'),
	url(r'^funcionario/delete/(?P<pk>\d+)$', funcionario_delete, name='funcionario_delete'),
	url(r'^funcionario/new/$', funcionario_new, name='funcionario_new'),

	#Rotas de professores
	url(r'^professor/list$', professor_list, name='professor_list'),
	url(r'^professor/detail/(?P<pk>\d+)$', professor_detail, name='professor_detail'),
	url(r'^professor/update/(?P<pk>\d+)$', professor_update, name='professor_update'),
	url(r'^professor/new/$', professor_new, name='professor_new'),

	#Rotas de frequencia
	url(r'^frequencia/new/$', frequencia_new, name='frequencia_new'),
	url(r'^frequencia/list$', frequencia_list, name='frequencia_list'),
	url(r'^frequencia/register/(?P<pk>\d+)$', frequencia_register, name='frequencia_register'),
	url(r'^frequencia/detail/(?P<pk>\d+)$', frequencia_detail, name='frequencia_detail'),

	url(r'^horario/professor/new/$', horario_professor_new, name='horario_professor_new'),
]

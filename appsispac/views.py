from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render,redirect
from appsispac.models import *
from appsispac.forms import *
from django.forms import formset_factory
# Create your views here.
def home(request):
    return render(request, 'base.html')

def funcionario_list(request):
    criterio = request.GET.get('criterio')
    if(criterio):
        funcionarios = Funcionario.objects.filter(nome__contains=criterio)
    else:
        funcionarios = Funcionario.objects.all().order_by('nome')
        criterio = ""
    paginator = Paginator(funcionarios, 5)
    page = request.GET.get('page')
    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)
    dados = {'funcionarios': funcionarios, 'criterio': criterio, 'paginator': paginator, 'page_obj':funcionarios}
    return render(request, 'funcionario/funcionario_list.html', dados)

def professor_list(request):
    criterio = request.GET.get('criterio')
    if(criterio):
        professores = Professor.objects.filter(nome__contains=criterio)
    else:
        professores = Professor.objects.all().order_by('nome')
        criterio = ""
    paginator = Paginator(professores,5)
    page = request.GET.get('page')
    try:
        professores = paginator.page(page)
    except PageNotAnInteger:
        professores = paginator.page(1)
    except EmptyPage:
        professores = paginator.page(paginator.num_pages)
    dados = {'professores':professores, 'criterio':criterio, 'paginator':paginator, 'page_obj':professores}
    return render(request, 'professor/professor_list.html', dados)
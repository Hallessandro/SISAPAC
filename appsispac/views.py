from calendar import weekday

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from appsispac.models import *
from appsispac.forms import *
from django.forms import formset_factory
import datetime as DT
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def erro_permissao(request):
    return render(request,'utils/permissao.html')

#Views de funcionario
@permission_required('appsispac.view_funcionario',login_url='erro_permissao')
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


@permission_required('appsispac.add_funcionario',login_url='erro_permissao')
def funcionario_new(request):
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST)
        if(form.is_valid()):
            funcionario = form.save()
            grupoFuncionario = Group.objects.get(name='funcionario')
            grupoFuncionario.user_set.add(funcionario)
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
    dados={'form':form}
    return render(request,'funcionario/funcionario_form.html',dados)

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@permission_required('appsispac.change_funcionario',login_url='erro_permissao')
def funcionario_update(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST,instance=funcionario)
        if (form.is_valid()):
            funcionario = form.save(commit=False)
            funcionario.username = funcionario.matricula
            funcionario.set_password(funcionario.senha)
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm(instance=funcionario)
    dados ={'form':form,'funcionario':funcionario}
    return render(request,'funcionario/funcionario_form.html',dados)

@permission_required('appsispac.delete_funcionario',login_url='erro_permissao')
def funcionario_delete(request,pk):
    funcionario=Funcionario.objects.get(id=pk)
    funcionario.delete()
    return redirect('funcionario_list')

@permission_required('appsispac.view_funcionario',login_url='login')
def funcionario_detail(request, pk):
    funcionario=Funcionario.objects.get(id=pk)
    return render(request, 'funcionario/funcionario_detail.html', {'funcionario':funcionario})

#Views de professor
@permission_required('appsispac.view_professor',login_url='erro_permissao')
def professor_list(request):
    criterio = request.GET.get('criterio')
    if(criterio):
        professores = Professor.objects.filter(nome__contains=criterio)
        horarios = []
        for h in Horario_Professor.objects.all():
            if(h.professor.nome.__contains__(criterio)):
                horarios.append(h)
    else:
        professores = Professor.objects.all().order_by('nome')
        horarios = Horario_Professor.objects.all()
        criterio = ""
    paginator = Paginator(professores,5)
    page = request.GET.get('page')
    try:
        professores = paginator.page(page)
    except PageNotAnInteger:
        professores = paginator.page(1)
    except EmptyPage:
        professores = paginator.page(paginator.num_pages)
    dados = {'professores':professores, 'criterio':criterio, 'paginator':paginator, 'page_obj':professores, 'horarios':horarios}
    return render(request, 'professor/professor_list.html', dados)

@permission_required('appsispac.view_professor',login_url='erro_permissao')
def professor_detail(request, pk):
    professor = Professor.objects.get(id=pk)
    horarios = []
    for h in Horario_Professor.objects.all():
        if(h.professor == professor):
            horarios.append(h)
    data = {'professor':professor, 'horarios':horarios}
    return render(request, 'professor/professor_detail.html', data)

@permission_required('appsispac.view_horarios',login_url='login')
def horario_detail(request, pk):
    horario = Horario_Professor.professor.objects.get(id=pk)
    return render(request, 'professor/professor_detail.html', {'horario':horario})

@permission_required('appsispac.add_professor',login_url='erro_permissao')
def professor_new(request):
    if(request.method=="POST"):
        form = ProfessorForm(request.POST)
        if(form.is_valid()):
            professor=form.save(commit=False)
            professor.username = professor.matricula
            professor.set_password(professor.senha)
            professor.save()
            grupoProfessor=Group.objects.get(name='professor')
            grupoProfessor.user_set.add(professor)

            return redirect('professor_list')
    else:
        form = ProfessorForm()
        dados = {'form':form}
        return render(request, 'professor/professor_form.html',dados)

@permission_required('appsispac.change_professor',login_url='erro_permissao')
def professor_update(request,pk):
    professor = Professor.objects.get(id=pk)
    if(request.method == "POST"):
        form = ProfessorForm(request.POST,instance=professor)
        if(form.is_valid()):
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)
    dados = {'form':form, 'professor':professor}
    return render(request, 'professor/professor_form.html', dados)

@permission_required('appsispac.delete_professor',login_url='login')
def professor_delete(request,pk):
    professor = Professor.objects.get(id=pk)
    professor.delete()
    return redirect('professor_list')

@permission_required('appsispac.add_horario_professor',login_url='erro_permissao')
def horario_professor_new(request):
    if(request.method == "POST"):
        form = HorarioProfessorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('professor_list')
    else:
        form = HorarioProfessorForm()
        dados = {'form':form}
        return render(request, 'horario/horario_form.html',dados)

@permission_required('appsispac.view_registro_frequencia',login_url='erro_permissao')
def frequencia_list(request):
    today = DT.date.today()
    dayofweek = today.strftime("%A")
    criterio = request.GET.get('criterio')
    day = ""
    if(dayofweek == "Monday"):
        day = "SEG"
    elif (dayofweek == "Tuesday"):
        day = "TER"
    elif (dayofweek == "Wednesday"):
        day = "QUA"
    elif (dayofweek == "Thursday"):
        day = "QUI"
    elif (dayofweek == "Friday"):
        day = "SEX"
    else:
        day = "Dia inválido"
    frequencias = Registro_Frequencia.objects.filter(horario__weekdays=day)
    paginator = Paginator(frequencias, 5)
    page = request.GET.get('page')
    try:
        frequencias = paginator.page(page)
    except PageNotAnInteger:
        frequencias = paginator.page(1)
    except EmptyPage:
        frequencias = paginator.page(paginator.num_pages)
    dados = {'frequencias': frequencias, 'paginator': paginator, 'page_obj': frequencias}
    return render(request, 'frequencia/frequencia_list.html', dados)

@permission_required('appsispac.view_registro_frequencia',login_url='erro_permissao')
def frequencia_list_geral(request):
    frequencias = Registro_Frequencia.objects.all()
    paginator = Paginator(frequencias, 5)
    page = request.GET.get('page')
    try:
        frequencias = paginator.page(page)
    except PageNotAnInteger:
        frequencias = paginator.page(1)
    except EmptyPage:
        frequencias = paginator.page(paginator.num_pages)
    dados = {'frequencias': frequencias, 'paginator': paginator, 'page_obj': frequencias}
    return render(request, 'frequencia/frequencia_list.html', dados)

@permission_required('appsispac.add_frequencia',login_url='erro_permissao')
def frequencia_new(request):
    today = DT.date.today()
    dayofweek = today.strftime("%A")
    day = ""
    if (dayofweek == "Monday"):
        day = "SEG"
    elif (dayofweek == "Tuesday"):
        day = "TER"
    elif (dayofweek == "Wednesday"):
        day = "QUA"
    elif (dayofweek == "Thursday"):
        day = "QUI"
    elif (dayofweek == "Friday"):
        day = "SEX"
    else:
        day = "Dia inválido"
    horarios = Horario_Professor.objects.filter(weekdays=day)
    frequencias = Registro_Frequencia.objects.all()
    for h in horarios:
        frequencia = Registro_Frequencia()
        frequencia.data_frequencia = today
        frequencia.sala = h.sala
        frequencia.horarios = h.horario
        frequencia.registro_frequencia = False
        frequencia.horario = h
        frequencia.save()

    return redirect('frequencia_list_geral')

@permission_required('appsispac.add_frequencia_register',login_url='erro_permissao')
def frequencia_register(request, pk):
    criterio = request.GET.get('criterio')
    if(criterio == "registrar"):
        frequencia = Registro_Frequencia.objects.get(id=pk)
        frequencia.registro_frequencia = True
        frequencia.data_registro = DT.date.today()
        frequencia.save()
    else:
        frequencia = Registro_Frequencia.objects.get(id=pk)
        frequencia.registro_frequencia = False
        frequencia.data_registro = None
        frequencia.save()
        cancelamento = Cancelamento_Registro()
        cancelamento.data_cancelamento = DT.date.today()
        cancelamento.nome = request.GET.get('nome')
        cancelamento.motivo = request.GET.get('motivo')
        cancelamento.registro = frequencia
        cancelamento.save()
    return redirect('frequencia_list')

@permission_required('appsispac.view_registro_frequencia',login_url='erro_permissao')
def frequencia_detail(request,pk):
    frequencia = Registro_Frequencia.objects.get(id=pk)
    cancelamentos = Cancelamento_Registro.objects.filter(registro=pk)
    #cancelamentos = Cancelamento_Registro.objects.filter(registro__registro_frequencia=frequencia.id)
    return render(request, 'frequencia/frequencia_detail.html', {'frequencia':frequencia, 'cancelamentos':cancelamentos})
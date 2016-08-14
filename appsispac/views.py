from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render,redirect
from appsispac.models import *
from appsispac.forms import *
from django.forms import formset_factory
# Create your views here.
def home(request):
    return render(request, 'base.html')

#Views de funcionario
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

def funcionario_new(request):
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm()
    dados={'form':form}
    return render(request,'funcionario/funcionario_form.html',dados)

def funcionario_update(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST,instance=funcionario)
        if (form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm(instance=funcionario)
    dados ={'form':form,'funcionario':funcionario}
    return render(request,'funcionario/funcionario_form.html',dados)

def funcionario_delete(request,pk):
    funcionario=Funcionario.objects.get(id=pk)
    funcionario.delete()
    return redirect('funcionario_list')

def funcionario_detail(request, pk):
    funcionario=Funcionario.objects.get(id=pk)
    return render(request, 'funcionario/funcionario_detail.html', {'funcionario':funcionario})

#Views de professor
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

def professor_detail(request, pk):
    professor = Professor.objects.get(id=pk)
    horarios = []
    for h in Horario_Professor.objects.all():
        if(h.professor == professor):
            horarios.append(h)
    data = {'professor':professor, 'horarios':horarios}
    return render(request, 'professor/professor_detail.html', data)

def horario_detail(request, pk):
    horario = Horario_Professor.professor.objects.get(id=pk)
    return render(request, 'professor/professor_detail.html', {'horario':horario})

def professor_new(request):
    if(request.method=="POST"):
        form = ProfessorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
        dados = {'form':form}
        return render(request, 'professor/professor_form.html',dados)

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

def funcionario_update(request,pk):
    funcionario = Funcionario.objects.get(id=pk)
    if(request.method=='POST'):
        form=FuncionarioForm(request.POST,instance=funcionario)
        if (form.is_valid()):
            form.save()
            return redirect('funcionario_list')
    else:
        form=FuncionarioForm(instance=funcionario)
    dados ={'form':form,'funcionario':funcionario}
    return render(request,'funcionario/funcionario_form.html',dados)
def professor_delete(request,pk):
    professor = Professor.objects.get(id=pk)
    professor.delete()
    return redirect('professor_list')

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


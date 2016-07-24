from django.shortcuts import render,redirect
from appsispac.models import *
from appsispac.forms import *
from django.forms import formset_factory
# Create your views here.
def home(request):
    return render(request,'appsispac/base.html')

def frequencias_list(request):
    frequencias=Frequencia.objects.all()
    return render(request, 'appsispac/frequencias_list.html', {'frequencias':frequencias})

def frequencias_update(request, pk):
    frequencias=Frequencia.objects.get(id=pk)
    if (request.method=="POST"):
        form=FrequenciaForm(request.POST,instance=frequencias)
        if(form.is_valid()):
            form.save()
            return redirect('frequencias_list')
    else:
        form=FrequenciaForm(instance=frequencias)
        dados={'form':form,'frequencias':frequencias}
    return render(request,'appsispac/frequencias_form.html',dados)

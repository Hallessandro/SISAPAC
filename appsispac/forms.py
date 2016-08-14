from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from appsispac.models import *
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields=('nome','matricula','senha')

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ('nome', 'matricula', 'senha')

class HorarioProfessorForm(ModelForm):
    class Meta:
        model = Horario_Professor
        fields = ('weekdays', 'horario', 'turma', 'disciplina','professor')

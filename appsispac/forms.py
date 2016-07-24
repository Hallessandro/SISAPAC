from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from appsispac.models import *

class FrequenciaForm(ModelForm):
   class Meta:
       model=Frequencia
       fields=('sala','disciplina', 'situacao')

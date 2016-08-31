from django.forms import ModelForm, forms
from django.forms.models import inlineformset_factory
from django import forms
from appsispac.models import *
from appsispac.utils import generate_hash_key
from appsispac.mail import send_mail_template
from .models import PasswordReset

class FuncionarioForm(ModelForm):
    #senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Funcionario
        fields=('nome','matricula','Email','senha')

'''
class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Funcionario.objects.filter(Email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário encontrado com este e-mail'
        )

    def save(self):
        funcionario = Funcionario.objects.get(Email=self.cleaned_data['email'])
        key = generate_hash_key(funcionario.username)
        reset = PasswordReset(key=key, user=funcionario)
        reset.save()
        template_name = 'login.htmL'
        subject = 'Criar nova senha no Simple MOOC'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [funcionario.Email])
'''

class ProfessorForm(ModelForm):
    #senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Professor
        fields = ('nome', 'matricula', 'senha')

class HorarioProfessorForm(ModelForm):
    class Meta:
        model = Horario_Professor
        fields = ('weekdays', 'horario', 'turma', 'disciplina','professor', 'sala')

class Registro_FrequenciaForm(ModelForm):
    class Meta:
        model = Registro_Frequencia
        fields = ('data_registro','data_frequencia','sala','horarios','registro_frequencia')
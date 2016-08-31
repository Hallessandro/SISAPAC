from django.db import models
from django.contrib.auth.models import User,Group
from django import forms
from django.conf import settings

class Funcionario(User):
    nome = models.CharField("Nome", max_length=200)
    matricula = models.IntegerField("Matricula",unique=False)
    Email = models.EmailField("E-Mail", max_length=200)
    senha = models.CharField(max_length=32)

    #class Meta:
     #   permissions = (('view_funcionario','can see funcionario'),)


    def __str__(self):
        return self.nome
'''
class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    verbose_name='Usuário',related_name='resets')
    key = models.CharField('Chave',max_length=100,unique=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    confirmed = models.BooleanField('Confirmado',default=False,blank=True)
    def __str__(self):
       return '{0} em {1}'.format(self.user,self.created_at)

    class Meta:
        verbose_name= 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering =['-created_at']
'''
class Professor(Funcionario):
    def __str__(self):
        return self.nome

   # class Meta:
    #    permissions = (('view_professor', 'can see professor'),)

class Sala(models.Model):
    sigla = models.CharField("Sigla", max_length=10)
    descricao = models.CharField("Descrição", max_length=100)
    def __str__(self):
        return self.sigla

    #class Meta:
     #   permissions = (('view_sala', 'can see salas'),)

class Horario_Professor(models.Model):
    WEEKDAYS = (
        ('ND', 'Não definido'),
        ('SEG', 'Segunda-Feira'),
        ('TER', 'Terça-Feira'),
        ('QUA', 'Quarta-Feira'),
        ('QUI', 'Quinta-Feira'),
        ('SEX', 'Sexta-Feira'),
    )
    weekdays = models.CharField(
        max_length=25,
        choices=WEEKDAYS,
        default='ND',
    )
    HORARIOS = (
        ('Vazio', 'Indefinido'),
        ('07:00 - 08:30', '07:00 - 08:30'),
        ('08:50 - 10:20', '08:50 - 10:20'),
        ('10:30 - 12:00', '10:30 - 12:00'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('14:50 - 16:20', '14:50 - 16:20'),
        ('16:30 - 18:00', '16:30 - 18:00'),
        ('18:00 - 19:50', '18:00 - 19:50'),
        ('20:00 - 22:00', '20:00 - 22:00'),
    )
    horario = models.CharField(
        max_length=30,
        choices=HORARIOS,
        default='Vazio',
    )
    turma = models.CharField("Turma", max_length=150)
    disciplina = models.CharField("Disciplina", max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    def __str__(self):
        return self.weekdays + " - " + self.horario

#    class Meta:
 #       permissions = (('view_horario_professor', 'can see Horario_professor'),)

class Registro_Frequencia(models.Model):
    data_registro = models.DateField("Data do registro", blank=True, null=True)
    #data_frequencia é o dia ao qual a frequência está relacionada
    data_frequencia = models.DateField("Data da frequência")
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    HORARIOS = (
        ('Vazio', 'Indefinido'),
        ('07:00 - 08:30', '07:00 - 08:30'),
        ('08:50 - 10:20', '08:50 - 10:20'),
        ('10:30 - 12:00', '10:30 - 12:00'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('14:50 - 16:20', '14:50 - 16:20'),
        ('16:30 - 18:00', '16:30 - 18:00'),
        ('18:00 - 19:50', '18:00 - 19:50'),
        ('20:00 - 22:00', '20:00 - 22:00'),
    )
    horarios = models.CharField(
        max_length=30,
        choices=HORARIOS,
        default='Vazio',
    )
    horario = models.ForeignKey(Horario_Professor, on_delete=models.PROTECT)
    registro_frequencia = models.BooleanField("Registro de Frequência", default=False)
    def __str__(self):
        return self.horario.professor.nome + " " + str(self.registro_frequencia)

   # class Meta:
    #    permissions = (('view_registro_frequencia', 'can see registro frequencia'),)

class Reserva_Sala(models.Model):
    data = models.DateField("Data do Registro")
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    HORARIOS = (
        ('Vazio', 'Indefinido'),
        ('07:00 - 08:30', '07:00 - 08:30'),
        ('08:50 - 10:20', '08:50 - 10:20'),
        ('10:30 - 12:00', '10:30 - 12:00'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('14:50 - 16:20', '14:50 - 16:20'),
        ('16:30 - 18:00', '16:30 - 18:00'),
        ('18:00 - 19:50', '18:00 - 19:50'),
        ('20:00 - 22:00', '20:00 - 22:00'),
    )
    horario = models.CharField(
        max_length=30,
        choices=HORARIOS,
        default='Vazio',
    )
    def __str__(self):
        return self.funcionario.nome

    #class Meta:
    #    permissions = (('view_reserva_Sala', 'can see reserva de sala'),)

class Cancelamento_Registro(models.Model):
    data_cancelamento = models.DateField("Data do cancelamento")
    nome = models.CharField("Nome", max_length=255)
    #Neste momento nome recebe um nome digitado, porém após implementar autenticação
    #ele deve receber o nome da pessoa na sessão atual
    motivo = models.CharField("Motivo", max_length=1000)
    registro = models.ForeignKey(Registro_Frequencia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


    #class Meta:
    #    permissions = (('view_cancelamento_registro', 'can see cancelamento_registro'),)

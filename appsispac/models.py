from django.db import models

# Create your models here.
class Professor(models.Model):
    matricula = models.CharField(max_length=12)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

class Horario(models.Model):
    HORARIOS = (
        ('Vazio', 'Indefinido'),
        ('1M', '07:00 - 08:30'),
        ('2M', '08:50 - 10:20'),
        ('3M', '10:30 - 12:00'),
        ('1T', '13:00 - 14:30'),
        ('2T', '14:50 - 16:20'),
        ('3T', '16:30 - 18:00'),
        ('1N', '18:00 - 19:50'),
        ('2N', '20:00 - 22:00'),
    )
    horarios = models.CharField(
        max_length=2,
        choices=HORARIOS,
        default='Vazio',
    )
    def __str__(self):
        return self.horarios

class Disciplina(models.Model):
    titulo = models.CharField(max_length=255)
    professor = models.ManyToManyField(Professor)
    horario = models.ManyToManyField(Horario)

    def __str__(self):
        return self.titulo

class Frequencia(models.Model):
    sala = models.CharField(max_length=30)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    SITUACAO = (
        ('NR', 'Aula não realizada'),
        ('AR', 'Aula realizada'),
    )
    situacao = models.CharField(max_length=2, choices=SITUACAO, default='NR')

    def __str_(self):
        return self.disciplina

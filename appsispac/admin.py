from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Funcionario)
admin.site.register(Professor)
admin.site.register(Sala)
admin.site.register(Registro_Frequencia)
admin.site.register(Reserva_Sala)
admin.site.register(Horario_Professor)
admin.site.register(Cancelamento_Registro)
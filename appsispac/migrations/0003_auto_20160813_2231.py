# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsispac', '0002_auto_20160813_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios',
            name='horarios',
            field=models.CharField(choices=[('Vazio', 'Indefinido'), ('07:00 - 08:30', '07:00 - 08:30'), ('08:50 - 10:20', '08:50 - 10:20'), ('10:30 - 12:00', '10:30 - 12:00'), ('13:00 - 14:30', '13:00 - 14:30'), ('14:50 - 16:20', '14:50 - 16:20'), ('16:30 - 18:00', '16:30 - 18:00'), ('18:00 - 19:50', '18:00 - 19:50'), ('20:00 - 22:00', '20:00 - 22:00')], default='Vazio', max_length=30),
        ),
    ]

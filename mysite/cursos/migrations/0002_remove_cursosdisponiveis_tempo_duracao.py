# Generated by Django 4.0.4 on 2022-05-17 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursosdisponiveis',
            name='tempo_duracao',
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aprendiz(models.Model):
    id_aprendiz = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='id_curso', verbose_name='ID_Curso')
    id_calificacion = models.ForeignKey('Calificaciones', models.DO_NOTHING, db_column='id_calificacion', verbose_name='ID_Calificacion')
    nombres = models.CharField(max_length=40, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.CharField(max_length=10, blank=True, null=True, verbose_name='Telefono')

    class Meta:
        managed = False
        db_table = 'aprendiz'


class Calificaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_aprendiz = models.IntegerField()
    id_curso = models.IntegerField()
    nota = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    id_aprendiz = models.IntegerField()
    curso = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'cursos'
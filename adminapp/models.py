from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
now = timezone.now()

@python_2_unicode_compatible
class Descicion(models.Model):
	des = models.CharField(max_length=9)

	def __str__(self):
		return self.des

@python_2_unicode_compatible
class Sexo(models.Model):
	sexo = models.CharField(max_length=9)

	def __str__(self):
		return self.sexo

@python_2_unicode_compatible
class Pais(models.Model):
	pais = models.CharField(max_length=50)

	def __str__(self):
		return self.pais

@python_2_unicode_compatible
class Depto(models.Model):
	depto = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __str__(self):
		return self.depto

@python_2_unicode_compatible
class Municipio(models.Model):
	municipio = models.CharField(max_length=50)
	depto = models.ForeignKey(Depto)

	def __str__(self):
		return self.municipio

@python_2_unicode_compatible
class TipoCentro(models.Model):
	tipo_centro = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo_centro

@python_2_unicode_compatible
class Zona(models.Model):
	zona = models.CharField(max_length=50)

	def __str__(self):
		return self.zona

@python_2_unicode_compatible
class Patrocinador(models.Model):
	nombre_patrocinador = models.CharField(max_length=70)
	direccion = models.CharField(max_length=70)
	telefono = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre_patrocinador

@python_2_unicode_compatible
class TipoPersona(models.Model):
	tipo_persona = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo_persona

@python_2_unicode_compatible
class GrupoEtnico(models.Model):
	grupo_etnico = models.CharField(max_length=70)

	def __str__(self):
		return self.grupo_etnico

@python_2_unicode_compatible
class Personas(models.Model):
	numid = models.CharField(max_length=15)	
	nombre = models.CharField(max_length=50)	
	apellido = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio)	
	domicilio = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9, blank=True, null=True)
	sexo = models.ForeignKey(Sexo)	
	tipo_persona = models.ForeignKey(TipoPersona)
	grupo_etnico = models.ForeignKey(GrupoEtnico)
	trabaja = models.ForeignKey(Descicion, related_name='trabaja')
	ocupacion = models.CharField(max_length=70)
	fecha_nacimiento = models.DateField(blank=True, null=True)
	edad = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "%s %s" %(self.nombre, self.apellido)
	
@python_2_unicode_compatible
class Centro(models.Model):
	centro = models.CharField(max_length=50)
	tipo_centro = models.ForeignKey(TipoCentro)
	patrocinador = models.ForeignKey(Patrocinador, blank=True, null=True)
	zona = models.ForeignKey(Zona, blank=True, null=True)
	patro_incentivo = models.ForeignKey(Descicion, related_name='Recibe_Incentivo')
	patro_recibe = models.CharField(max_length=50, blank=True, null=True)
	cada_cuando = models.CharField(max_length=50, blank=True, null=True)
	promotor = models.ForeignKey(Personas, blank=True, null=True)
	donde_funciona = models.CharField(max_length=50, blank=True, null=True)
	municipio = models.ForeignKey(Municipio)
	direccion = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.centro


@python_2_unicode_compatible
class TipoResidencia(models.Model):
	tipo_residencia = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo_residencia


@python_2_unicode_compatible
class Facilitador(models.Model):
	numid = models.CharField(max_length=15)	
	nombre = models.CharField(max_length=50)	
	apellido = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio)	
	tipo_residencia = models.ForeignKey(TipoResidencia)
	domicilio = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9, blank=True, null=True)
	sexo = models.ForeignKey(Sexo)	
	correo = models.EmailField(blank=True, null=True)
	ocupacion = models.CharField(max_length=70, blank=True, null=True)
	lugar_trabajo = models.CharField(max_length=70, blank=True, null=True)
	formacion_academica = models.CharField(max_length=70, blank=True, null=True)
	fecha_nacimiento = models.DateField(blank=True, null=True)
	edad = models.IntegerField(blank=True, null=True)
	fecha_llenado = models.DateField(blank=True, null=True)
	tiempo_facilitador = models.DateField(blank=True, null=True)
	becado = models.ForeignKey(Descicion, related_name='becado')
	estudia = models.ForeignKey(Descicion, related_name='estudia')
	donde_estudia = models.CharField(max_length=70, blank=True, null=True)
	que_estudia = models.CharField(max_length=70, blank=True, null=True)

	def __str__(self):
		return "%s %s" %(self.nombre, self.apellido)


@python_2_unicode_compatible
class Grado(models.Model):
	grado = models.CharField(max_length=50)
	facilitador = models.ForeignKey(Facilitador)

	def __str__(self):
		return self.grado

@python_2_unicode_compatible
class Periodo(models.Model):
	num_periodo = models.CharField(max_length=100)

	def __str__(self):
		return self.num_periodo

@python_2_unicode_compatible
class Matricula(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	persona = models.ForeignKey(Personas)
	centro = models.ForeignKey(Centro)
	grado = models.ForeignKey(Grado)
	num_periodo = models.ForeignKey(Periodo, related_name='Num_Periodo')
	horario = models.CharField(max_length=80, blank=True, null=True)
	inicio_clases = models.DateField(blank=True, null=True)
	fin_clases = models.DateField(blank=True, null=True)
	requisito = models.FileField(upload_to='imagenes')

	def __str__(self):
		return "%s %s" %(self.persona.nombre, self.grado.grado)

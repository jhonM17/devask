from django.db import models

# Create your models here.

#Modelo Tag
class Tag(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

#Modelo Pregunta
class Pregunta(models.Model):
	nombre = models.CharField(max_length=50)
	contenido = models.TextField(max_length=200)
	tag = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.nombre


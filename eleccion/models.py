from django.db import models

# Create your models here.
class Circunscripcion(models.Model):
	nombre = models.CharField(max_length = 144, default = "nombre")
	nEscanos = models.IntegerField(blank=True)
	
	class Meta:
		ordering = ['nombre']
	
	def __unicode__(self):
		return self.nombre

class Mesa(models.Model):
	nombre = models.CharField(max_length = 144, default = "nombre")
	circunscripcion = models.ForeignKey(Circunscripcion)

	class Meta:
<<<<<<< HEAD
		ordering = ['circunscripcion', 'nombre']
=======
		ordering = ['nombre']
>>>>>>> 822b6fcf9cb61481a4a27938c8135354d8aecb02

	def __unicode__(self):
		return 'Mesa: %s, De: %s' % (self.nombre, self.circunscripcion)

	
class Partido(models.Model):
	nombre = models.CharField(max_length = 144, default = "nombre", unique = True)

	class Meta:
		ordering = ['nombre']
		
	def __unicode__(self):
		return self.nombre

class Resultado(models.Model):
	partido = models.ForeignKey(Partido)
	mesa = models.ForeignKey(Mesa)
	nVotos = models.IntegerField(blank = True)

	def __unicode__(self):
		return 'Partido: %s, + Mesa: %s --> %s votos' % (self.nombre, self.mesa, self.nVotos)


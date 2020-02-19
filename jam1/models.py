from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

##--------MODELO DE EVENTO-------##
class Event(models.Model):
	#clase que define a los eventos. los mismos son creados por un usuario que invita a otros usuarios.

	fecha_creacion = models.DateTimeField(auto_now_add=True)

	usuario_creador=models.OneToOneField(User, on_delete=models.CASCADE)

	usario_añadido= models.ManyToManyField(User, related_name= "usuario_añadido2")
	
	lugar=models.CharField(max_length=100)
	
	descripcion=models.CharField(max_length=300)
	
	tipos=(('Abierto','Abierto'),('Cerrado','Cerrado'))
	
	tipo = models.CharField(max_length=30, choices=tipos)

	def __str__(self):
		return " lugar: {} , fecha_creacion:  {} " .format(self.lugar, self.fecha_creacion)



#------Modelo de Profile-------#

class Profile(models.Model):
	#modelo que conecta el profile con el usuario y contiene caracteristicas inerentes al musico

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	instrument= models.CharField(max_length= 100)
	
	choices_jam_place= (('Tienes un lugar para juntarse','Tienes un lugar para juntarse'),('No tienes lugar para juntarse','No tienes lugar para juntarse'))
	jam_place= models.CharField(max_length= 50, choices= choices_jam_place)
	
	location=models.CharField(max_length=100)
	
	choices_nivel=(('Amateur','Amateur'),('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado'),('Profesional','Profesional'))	
	nivel = models.CharField(max_length=30, choices=choices_nivel)
	
	comment= models.CharField(max_length= 50)

	def __str__(self):
		return " User: {} , Instrument:  {} " .format(self.user, self.instrument)



class Intereses(models.Model):
	#Filtro general de intereses. Los intereses deben ser a priori las disintas categorias.

	Categoria= models.CharField(max_length=50)

	Nombre=models.CharField(max_length=30)




###_-------------------clase de Señales para token--------------------#####

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
##        Token.objects.create(user=instance)
#
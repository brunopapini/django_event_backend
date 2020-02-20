from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from location_field.models.plain import PlainLocationField

##modelos de la aplicacion para jamear##

##--------MODELO DE EVENTO-------##




class Event(models.Model):
	#clase que define a los eventos. los mismos son creados por un usuario que invita a otros usuarios.

	#fecha de creacion del evento
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	#Usuario que crea el evento
	usuario_creador=models.OneToOneField(User, on_delete=models.CASCADE)

	#Usuarios añadidos al evento. solo pueden ser añadidos por el usuario creador.
	usario_añadido= models.ManyToManyField(User, related_name= "usuario_añadido2")
	

	#lugar donde se realizara el evento
	lugar=models.CharField(max_length=100)
	
	#descripcion general del evento
	descripcion=models.CharField(max_length=300)
	
	#definicion del tipo de evento, ya si es abierto o cerrado.
	tipos=(('Abierto','Abierto'),('Cerrado','Cerrado'))
	tipo = models.CharField(max_length=30, choices=tipos)

	#metodo que devuelve string 
	def __str__(self):
		return " lugar: {} , fecha_creacion:  {} " .format(self.lugar, self.fecha_creacion)




###--------clase que engloba los Intereses existentes-----####
class Intereses(models.Model):
	#Filtro general de intereses. Los intereses deben ser a priori las disintas categorias.

	Categoria= models.CharField(max_length=50)

	Nombre=models.CharField(max_length=30)

	class Meta:
		ordering = [ 'Categoria','Nombre']

	def __str__(self):
		return " Categoria: {} , Género:  {} " .format(self.Categoria, self.Nombre)

#####-------CLASE INSTRUMENT---------#####

class Instrument(models.Model):
		#"clase que contempla todos los instrumentos"
	nombre = models.CharField(max_length = 40)

	class Meta:
		ordering = ['nombre']



	def __str__(self):
		return " Instrument : {} " .format(self.nombre)





#------Modelo de Profile-------#

class Profile(models.Model):
	#modelo que conecta el profile con el usuario y contiene caracteristicas inerentes al musico

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name= models.CharField(max_length = 50)
	age = models.PositiveIntegerField()
	image= models.ImageField(default="default.jpg")


	#Intereses musciales
	intereses= models.ManyToManyField(Intereses)

	#instrumentos que poseo
	instruments= models.ManyToManyField(Instrument)
	
	
	#definiir si tiene un lugar para tocar
	choices_jam_place= (('Tienes un lugar para juntarse','Tienes un lugar para juntarse'),('No tienes lugar para juntarse','No tienes lugar para juntarse'))
	jam_place= models.CharField(max_length= 50, choices= choices_jam_place)
	
	#ubicacion en la que vive
	city = models.CharField(max_length=255)
	location = PlainLocationField(based_fields=['city'], zoom=7)


	#nivel de musica
	choices_nivel=(('Amateur','Amateur'),('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado'),('Profesional','Profesional'))	
	nivel = models.CharField(max_length=30, choices=choices_nivel)
	

	#descripcion que quiere que vean los demas sobre el mismo
	comment= models.CharField(max_length= 50)


	#eventos en los que esta adherido
	event_suscribe= models.ManyToManyField(Event, blank=True)


	# metodo que retorna el string
	def __str__(self):
		return " User: {} " .format(self.user)







###_-------------------clase de Señales para token--------------------#####

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
##        Token.objects.create(user=instance)
#
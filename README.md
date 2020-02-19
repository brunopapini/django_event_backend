# django_event_backend
Backend for mobile app in django. 

This package create endpoints for User authentication in Django for a POST method with User/email and password.
Retrieves a token key used to make an authenticated GET request

Django Api Rest token - Flutter
BackEnd(Django, Api-Rest Tokend) Android Flutter

Comandos Utilizados

Crear Aplicacion
python manage.py Jam app

Crear un Super Usuario
python src/manage.py createsuperuser

Ejecutar el proyecto
python src/manage.py runserver 0.0.0.0:8000

Crear migraciones
python src/manage.py makemigrations
actualizar base de datos
python src/manage.py migrate


Installed Apps:
Django rest framework 
Django rest framework auth
Jam


To runserver local

Open Command Prompt

folder with manage.py file ( django_event_backend)

To runserver locally:

1) pyhton manage.py runserver


To run the server and access from a remote endpoint:

1) add your IPV4 terminal to allowed host in settings.py

2) python manage.py runserver 192.168.***.*:8000







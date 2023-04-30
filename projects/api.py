"""
? Crear las vistas: 
despues de haber creado los serializers, se deben crear 

las vistas que se utilizarán para procesar las solicitudes HTTP 
y enviar las respuestas correspondientes. 

Las vistas se encargan de acceder a los datos a través del ORM de Django 
y transformarlos utilizando los serializers antes de enviarlos como respuesta."""

from .models import Project
from rest_framework import viewsets,permissions
from .serializers import Projectserializer

class Projectviewset(viewsets.ModelViewSet):
    # define una nueva clase llamada "Projectviewset" que hereda de la clase "viewsets.ModelViewSet" de DRF.

    queryset = Project.objects.all()
    # define el conjunto de consultas (queryset)
    # que se utilizará para obtener los datos de la base de datos.
    
    # En este caso, usa el modelo "Project"
    # y se recuperan todos los objetos de la base de datos.

    permission_classes = [permissions.AllowAny]
    # define las clases de permisos que se aplicarán a la vista.
    # En este caso, se permite el acceso a cualquier usuario
    # sin autenticación (permiso "AllowAny").

    serializer_class = Projectserializer
    # Esto define la clase de serializador que se utilizará
    # para convertir los objetos del modelo en JSON (y viceversa).

    # En este caso, usa el serializador "Projectserializer"
    # definido en el archivo serializers.py.
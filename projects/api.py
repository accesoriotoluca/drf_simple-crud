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

    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Projectserializer
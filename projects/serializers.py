"""
? Crear los serializers: 
Una vez que se han creado los modelos, 
se deben crear los serializers que se 

encargarán de transformar los datos de los modelos en formatos que puedan ser consumidos por la API. 
Los serializers son responsables de la validación de los datos y la conversión de los mismos 
en formatos estándar como JSON o XML."""

from rest_framework import serializers
from .models import Project

class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','description','technology','created_at')
        read_only_fields = ('created_at',)
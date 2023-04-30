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
    #se define una clase llamada "Projectserializer" que hereda de "serializers.ModelSerializer". 
    # Esta clase se utilizará para definir cómo se serializan y deserializan los datos del modelo "Project".

    class Meta:
        model = Project
        fields = ('id','title','description','technology','created_at')
        read_only_fields = ('created_at',)
        #se define una clase interna llamada "Meta". 
        # Esta clase se utiliza para definir la configuración del serializador. 
        # En este caso, el modelo que se utilizará es "Project". 
        # Los campos que se incluirán en la respuesta de la API son 'id', 'title', 'description', 'technology' y 'created_at'. 
        # Además, se establece que el campo 'created_at' será de solo lectura, 
        # lo que significa que no se puede actualizar a través de la API.
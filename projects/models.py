"""
? Crear los modelos: 
En primer lugar, se deben crear los modelos que representan los datos que se utilizarán en la API.
Estos modelos pueden ser creados utilizando el ORM de Django,
lo que permite definir la estructura de la base de datos y las relaciones entre las diferentes 'entidades'."""

from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
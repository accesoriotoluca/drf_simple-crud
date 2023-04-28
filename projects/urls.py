"""
? Crear las URLs: 
Una vez que se han creado las vistas apis.py,

se deben definir las URLs que se utilizarán para 
acceder a las diferentes rutas de la API. 

Las URLs se definen utilizando el enrutador de Django 
y se asocian con las vistas correspondientes.

*configurar tu API RESTful en el archivo urls.py de tu aplicación es una buena práctica en Django, especialmente si estás utilizando el enfoque de "URLs basadas en clases" con Django Rest Framework. Esto te permite separar la lógica de tu API de la lógica de tu aplicación y tener un mayor control sobre cómo se mapean las URL a las vistas.

este código configura una API RESTful en Django
utilizando el enrutador predeterminado de DRF (DefaultRouter).
La URL /api/projects/ se asocia con la vista de conjunto (viewset) Projectviewset,
y todas las URL generadas por el enrutador se guardan en la variable urlpatterns """

from rest_framework import routers
from .api import Projectviewset

router = routers.DefaultRouter()
#Aquí, estamos creando una instancia del enrutador predeterminado de DRF (DefaultRouter) y guardando la instancia en la variable router.

router.register('api/projects',Projectviewset,'projects')
# estamos usando el método register() del enrutador para asociar URL /api/projects/ con 'vista de conjunto' (viewset) Projectviewset
# La cadena 'projects' es opcional, se usa para nombrar el conjunto de vistas (viewset) registrado.
"""
? prefix: 'api/projects'
la URL del prefijo que se utilizará para asociar la vista de conjunto.

* viewset: Projectviewset
la vista de conjunto (viewset) que se utilizará para manejar las solicitudes HTTP relacionadas con esta URL.

?basename: 'projects'
el nombre que se utilizará para identificar esta vista de conjunto (viewset) en el enrutamiento inverso (reverse routing). Este parámetro es opcional.
"""

urlpatterns = router.urls
# estamos guardando todas las URL generadas por el enrutador en la variable urlpatterns. Esto es posible gracias al atributo urls del enrutador, que devuelve una lista de objetos URLPattern listos para ser utilizados en la aplicación Django.
from .models import Project
from rest_framework import viewsets,permissions
from .serializers import Projectserializer

class Projectviewset(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Projectserializer
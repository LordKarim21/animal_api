from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .models import Animal
from .serializer import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAdminOrReadOnly]

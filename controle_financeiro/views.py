from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

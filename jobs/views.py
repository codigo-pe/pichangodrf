from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import viewsets, permissions

class Canchas(viewsets.ModelViewSet):
     queryset = Cancha.objects.all()
     serializer_class = CanchaSerializer
     #permission_classes= (permissions.IsAuthenticated,)
    
class Juegos(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoListSerializer
    #permission_classes= (permissions.IsAuthenticated,)

class Formjuegos(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = FormjuegosListSerializer
    #permission_classes= (permissions.IsAuthenticated,)



# Create your views here.

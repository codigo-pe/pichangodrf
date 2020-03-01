from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import viewsets, permissions

class CanchasList(viewsets.ModelViewSet):
     queryset = Cancha.objects.all()
     serializer_class = CanchaSerializer
     #permission_classes= (permissions.IsAuthenticated,)
    
class JuegosList(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    #permission_classes= (permissions.IsAuthenticated,)



# Create your views here.

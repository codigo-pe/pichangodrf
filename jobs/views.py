from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import viewsets, permissions

from rest_framework.views import APIView
from django.contrib.auth import authenticate
import json

#Autentificación
from rest_framework.authtoken.models import Token

# Generar tokens para todos los usuarios
for user in User.objects.all():
    Token.objects.get_or_create(user=user)


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


class LoginView(APIView):
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            data = {"token": user.auth_token.key} 
        else:
            data = {"error": "No Son las Credenciales"}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta,content_type='application/json')




# Create your views here.

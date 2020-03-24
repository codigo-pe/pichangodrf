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

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


# Generar Auth tokens para todos los usuarios
for user in User.objects.all():
    Token.objects.get_or_create(user=user)

class Canchas(viewsets.ModelViewSet):
     queryset = Cancha.objects.all()
     serializer_class = CanchaSerializer
     #permission_classes= (permissions.IsAuthenticated,)
    
class Juegos(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoListSerializer

class Formjuegos(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = FormjuegosListSerializer



# Vista de todos los jugadores
#***************************************
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileOrReadOnly

class JugadorProfileListCreateView(ListCreateAPIView):
    queryset=Jugador.objects.all()
    serializer_class=JugadorProfileSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

#Vista de un jugador en específico
class JugadorProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Jugador.objects.all()
    serializer_class=JugadorProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

#*********************************************

#API LOGIN utilizando clases
class LoginView(APIView):
    # Generar Auth tokens para todos los usuarios
    # for user in User.objects.all():
    #     Token.objects.get_or_create(user=user)    
    permission_classes = (permissions.AllowAny,)
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.get_or_create(user=username)
            data = {"token": user.auth_token.key} 
        else:
            data = {"error": "No Son las Credenciales XD"}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta,content_type='application/json')

# API login basada en funciones
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Por favor ingrese usuario y contraseña'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Credenciales inválidas'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)


# Create your views here.
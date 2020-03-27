from rest_framework import serializers, viewsets
from .models import Cancha, Jugador, Juego
from django.contrib.auth.models import User

#Serializadores permite que los datos complejos tales como los query sets y instancias de un modelo puedan ser
#fácilmente convertidos a JSON XML u otro tipo de contenido 


#Serializer creado para mostrar el registro de jugadores
class JugadorProfileSerializer(serializers.ModelSerializer):
    usuario=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Jugador
        fields='__all__'

#Serializer creado para mostrar nombre y apellido en la lista de jugadores registrados en un juego
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

# Serializer creado para mostrar la descripcion de cada jugador registrado en un juego
class JugadorSerializer(serializers.ModelSerializer):
     usuario = UsuarioSerializer()
     class Meta:
         model = Jugador
         fields = ['usuario','distrito','posicion','descripcion']

#Serializer creado para mostrar la información de todos los juegos registrados
class JuegoSerializer(serializers.HyperlinkedModelSerializer):
    jugadores = JugadorSerializer(many=True,read_only=True)
    class Meta:
        model = Juego
        fields = ['id','estado','fecha','hora','descripcion','jugadores']


#Serializer para mostrar todas las canchas registradas en la aplicación
class CanchaSerializer(serializers.HyperlinkedModelSerializer):
     juegos=JuegoSerializer(many=True,read_only=True)
     class Meta:
         model = Cancha
         fields = ['id','nombre','direccion','distrito','costo_por_hora','jugadores_por_equipo','teléfono','Ubicación','juegos']
#         def create(self, validated_data):
#         tracks_data = validated_data.pop('tracks')
#         album = Album.objects.create(**validated_data)
#         for track_data in tracks_data:
#             Track.objects.create(album=album, **track_data)
#         return album

class CanchajuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = ['id','nombre','direccion','distrito','costo_por_hora','jugadores_por_equipo','teléfono','Ubicación']

class JuegoListSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True)
    cancha = CanchajuegoSerializer()
    class Meta:
        model = Juego
        fields = ['id','estado','fecha','hora','descripcion','jugadores','cancha']

class FormjuegosListSerializer(serializers.ModelSerializer):
    cancha= serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Juego
        fields = ['id','estado','fecha','hora','descripcion','cancha']


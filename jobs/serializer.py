from rest_framework import serializers, viewsets
from .models import Cancha, Jugador, Juego

#Serializadores permite que los datos complejos tales como los query sets y instancias de un modelo puedan ser
#fácilmente convertidos a JSON XML u otro tipo de contenido 

class JugadorSerializer(serializers.ModelSerializer):
     class Meta:
         model = Jugador
         fields = ['telefono','distrito','posicion','descripcion']

class JuegoSerializer(serializers.HyperlinkedModelSerializer):
    jugadores = JugadorSerializer(many=True,read_only=True)
    class Meta:
        model = Juego
        fields = ['id','estado','fecha','hora','descripcion','jugadores','cancha']
    
class CanchaSerializer(serializers.ModelSerializer):
     juegos=JuegoSerializer(many=True, read_only=True)
     class Meta:
         model = Cancha
         fields = ['id','nombre','direccion','distrito','costo_por_hora','jugadores_por_equipo','teléfono','Ubicación','juegos']
#         def create(self, validated_data):
#         tracks_data = validated_data.pop('tracks')
#         album = Album.objects.create(**validated_data)
#         for track_data in tracks_data:
#             Track.objects.create(album=album, **track_data)
#         return album
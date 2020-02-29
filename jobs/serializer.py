from rest_framework import serializers, viewsets
from .models import Cancha

#Serializadores permite que los datos complejos tales como los query sets y instancias de un modelo puedan ser
#fácilmente convertidos a JSON XML u otro tipo de contenido 

class CanchaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancha
        fields = ('nombre','direccion','distrito','costo_por_hora','jugadores_por_equipo','teléfono','Ubicación','id')

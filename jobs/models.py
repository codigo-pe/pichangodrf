from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cancha(models.Model):
    DISTRIT = (
    ('Comas','Comas'),
    ('Los Olivos','Los Olivos'),
    ('San Martín de Porres','San Martín de Porres'),
    )
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    distrito=models.CharField(max_length=100,choices= DISTRIT)
    telefono=models.CharField(max_length=20,name='teléfono')
    ubicacion=models.CharField(max_length=500,name='Ubicación', null=True)
    costoHora=models.DecimalField(decimal_places=2,max_digits=6,name='costo_por_hora', null=True)
    jugadoresMaximos=models.IntegerField(name='jugadores_por_equipo', null=True)
    
    def  __str__(self):
        return self.nombre

class Jugador(models.Model):
    DISTRIT = (
    ('Comas','Comas'),
    ('Los Olivos','Los Olivos'),
    ('San Martín de Porres','San Martín de Porres'),
    )
    POSITION =(
    ('Arco','Arco'),
    ('Defensa','Defensa'),
    ('Mediocampo','Mediocampo'),
    ('Ataque','Ataque'),
    ('Mixto','Mixto'),
    )
    usuario=models.OneToOneField(User, related_name= 'usuario', on_delete=models.CASCADE)
    telefono=models.CharField(max_length=20, null=True)
    distrito=models.CharField(max_length=100,choices= DISTRIT, null=True) 
    posicion=models.CharField(max_length=20,choices= POSITION,null=True)
    descripcion=models.TextField(null=True)

    def  __str__(self):
        return self.usuario.username

class Juego(models.Model):
    STATUS = (
    ('Activo','Activo'),
    ('Realizado','Realizado'),
    ('Cancelado','Cancelado'),
    )
    estado=models.CharField(max_length=100,choices= STATUS)
    fecha=models.DateField()
    hora=models.TimeField()
    cancha=models.ForeignKey(Cancha,related_name='juegos',on_delete=models.CASCADE)
    jugadores=models.ManyToManyField(Jugador,related_name='jugadores')
    descripcion=models.TextField(null=True)

    def  __str__(self):
        return self.cancha.nombre
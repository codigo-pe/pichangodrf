from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Jugador

@receiver(post_save, sender=User)
def create_jugador(sender, instance, created, **kwargs):
    if created:
        Jugador.objects.create(usuario=instance)
@receiver(post_save, sender=User)
def save_jugador(sender, instance, **kwargs):
    instance.usuario.save()

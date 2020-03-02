from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('canchaslist',views.Canchas)
router.register('juegoslist',views.Juegos)
urlpatterns = [
    path('',include(router.urls))

]

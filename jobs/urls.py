"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('canchaslist',views.Canchas)
router.register('juegoslist',views.Juegos)
router.register('formjuegos',views.Formjuegos)
urlpatterns = [
    path('',include(router.urls)),
    #Vista login
    path('login/',views.LoginView.as_view()),
    # Vista basada en funciones, se reemplazó por la vista login basada en clases
    # path('login/',views.login),
    #vista logout
    path('logout/', views.LogoutView.as_view()),
    #gets all user profiles and create a new profile
    path("all-profiles/",JugadorProfileListCreateView.as_view(),name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",JugadorProfileDetailView.as_view(),name="profile"),
    
]

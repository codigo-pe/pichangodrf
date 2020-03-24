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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # Rutas de Web token
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh', TokenRefreshView.as_view()),
    
    #path to djoser end points se instaló con pip install djoser
    # La ruta djoser para registrar usuarios es auth/users/. También acepta el método get, pero solo el superusuario (token del superusuario) tiene acceso a la lista de ususarios.
    # La ruta djoser para visualizar y modificar los datos del usuario es auth/users/me, solo se puede acceder con el token del propio usuario.
    path('auth/', include('djoser.urls')),

]

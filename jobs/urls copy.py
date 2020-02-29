from django.urls import path
from . import views
from rest_framework import routers
from jobs.views import *

router = routers.DefaultRouter()
router.register('servicioshelper',views.HelperList)
urlpatterns = [
    path('register/', views.registerPage, name ="register"),
    path('login/', views.loginPage, name ="login"),
    path('logout/', views.logoutUser, name ="logout"),

    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('inicia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),


    path('', views.home, name ="home"),
    path('listajuegos/', views.listajuegos, name ="listajuegos"),
    path('buscajuegos/', views.buscajuegos, name ="buscajuegos"),
    path('buscacanchas/', views.buscacanchas, name ="buscacanchas"),
    path('listajuegos/<int:juego_id>', views.detail,name='detail'),
    path('creajuego/', views.creajuego,name='creajuego'),
    path('creajuego/<int:juego_id>', views.inscripcion,name='inscripcion'),
    path('salirdejuego/<int:juego_id>', views.salirdejuego,name='salirdejuego'),
    path('listacanchas/', views.listacanchas, name ="listacanchas"),
    path('listacanchas/<int:cancha_id>', views.cancha_detail,name='cancha_detail'),
    path('accounts/profile/', views.profile,name='profile')
]


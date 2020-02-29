from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('canchaslist',views.CanchasList)
urlpatterns = [
    path('',include(router.urls))

]

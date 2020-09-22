from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Planet import views
from rest_framework import routers

planet_router = routers.DefaultRouter()
planet_router.register('',views.PlanetViewSet)

urlpatterns= [
    path('planet/',include(planet_router.urls))
]

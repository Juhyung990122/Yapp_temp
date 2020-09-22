from django.shortcuts import render
from Planet.models import Planet
from Planet.serializer import PlanetSerializer
from rest_framework import viewsets

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
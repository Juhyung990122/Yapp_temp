from django.shortcuts import render
from Ect.models import Trashcan,Token
from Ect.serializer import TrashcanSerializer, TokenSerializer
from rest_framework import viewsets

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer



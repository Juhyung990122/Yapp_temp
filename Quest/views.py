from django.shortcuts import render
from Quest.models import Quest
from Quest.serializer import QuestSerializer
from rest_framework import viewsets

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MgmtUserSerializer,FeedSerializer,QuestListSerializer
from .models import MgmtUser,Feed,QuestList

class MgmtUserViewSet(viewsets.ModelViewSet):
    queryset = MgmtUser.objects.all()
    serializer_class = MgmtUserSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    
    def perform_create(self,serializer):
        serializer.save(uid = self.request.user)

class QuestListViewSet(viewsets.ModelViewSet):
    queryset = QuestList.objects.all()
    serializer_class = QuestListSerializer
    
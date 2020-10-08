from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def rank_update(request):
    user_info = CustomUser.objects.all()
    serializer = UserSerializer(user_info)
    serializer.rank_save(user_info)
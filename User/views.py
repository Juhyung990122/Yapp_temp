from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MgmtUserSerializer,FeedSerializer,QuestListSerializer
from .models import MgmtUser,Feed,QuestList

class MgmtUserViewSet(viewsets.ModelViewSet):
    queryset = MgmtUser.objects.all()
    serializer_class = MgmtUserSerializer

    def update(self, request, *args, **kwargs): 
        nickname = request.data.get('nickname') 
        user_info  = self.get_object() #id로 들어온 객체 받아와서
        user_info.nickname = nickname #닉네임 저장
        self.perform_update(user_info) #객체 업데이트
        return Response(status=status.HTTP_201_CREATED)

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def perform_create(self,serializer):
        serializer.save(uid = self.request.email)

class QuestListViewSet(viewsets.ModelViewSet):
    queryset = QuestList.objects.all()
    serializer_class = QuestListSerializer


@api_view(['GET'])
def rank_update(request):
    user_info = MgmtUser.objects.all()
    serializer = MgmtUserSerializer(user_info)
    serializer.rank_save(user_info)
    return Response(serializer.data)
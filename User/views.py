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
def calculate_rank(request, user_id):
    if request.method == 'GET':
        user_info = MgmtUser.objects.all()
        serializer = MgmtUserSerializer(user_info, many = True)
        for user_info in user_info:
            serializer.rank_save(user_info)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        #except:
        #    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
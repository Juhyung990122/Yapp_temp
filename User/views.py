from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializer import MgmtUserSerializer,FeedSerializer,QuestListSerializer
from .models import MgmtUser,Feed,QuestList
import datetime

class MgmtUserViewSet(viewsets.ModelViewSet):
    queryset = MgmtUser.objects.all()
    serializer_class = MgmtUserSerializer

    def update(self, request, *args, **kwargs): 
        nickname = request.data.get('nickname') 
        users = MgmtUser.objects.all()
        for user in users:
            if user.nickname == nickname:
                return Response(status=status.HTTP_409_CONFLICT)
 
        user_info  = self.get_object()
        user_info.nickname = nickname 
        self.perform_update(user_info) 
        return Response(status=status.HTTP_201_CREATED)

    #lastlogined 갱신(앱실행시 호출)
    @action(detail=True, methods=['get'])
    def update_lastlogined(self, request, pk, *args, **kwargs):
        user_info = self.get_object()
        user_info.lastlogined = datetime.datetime.now()
        user_info.state = "N"
        self.perform_update(user_info)
        return Response(status=status.HTTP_201_CREATED)


    #신고기능_유저
    @action(detail=True, methods=['get'])
    def report_user(self,request, pk, *args, **kwargs):
        user_info = self.get_object()
        user_info.report_user_cnt += 1
        self.perform_update(user_info)

        if user_info.report_user_cnt >= 3:
            #self.perform_destroy(user_info)
            user_info.state = "L"
            serializer = self.get_serializer(user_info)
            return Response(serializer.data)    

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    #신고기능_피드
    @action(detail=True, methods=['get'])
    def report_feed(self,request, pk, *args, **kwargs):
        feed_info = self.get_object()
        report_user = MgmtUser.objects.get(id=request.user.id)

        #중복방지
        if str(report_user.id) not in feed_info.report_uidList: 
            feed_info.report_uidList.append(report_user.id)
            self.perform_update(feed_info)
            #3번째 신고면 삭제
            if len(feed_info.report_uidList) >= 3: 
                self.perform_destroy(feed_info)
                return Response(status = status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET'])
def level_update(request,pk):
    user_info = MgmtUser.objects.get(id = pk)
    serializer = MgmtUserSerializer(user_info)
    serializer.level_save(user_info)
    return Response(serializer.data,status = status.HTTP_202_ACCEPTED)
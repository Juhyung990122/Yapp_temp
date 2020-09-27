from User.models import MgmtUser, Feed, QuestList
from rest_framework import serializers
from .models import QuestList
from rest_framework.fields import CurrentUserDefault

class MgmtUserSerializer(serializers.ModelSerializer):
    '''
    - 기본제공 필드(필요한것만 걸러쓰기)
    "id"
    "password"
    "last_login"
    "is_superuser"
    "username"
    "first_name"
    "last_name"
    "email"
    "is_staff"
    "is_active"
    "date_joined"
    '''
    class Meta:
        model = MgmtUser
        fields = '__all__'
  
    def rank_save(self, user_info):
        qnum_list = QuestList.objects.values('uid').filter(state = "DONE")
        #요청유저 퀘스트 숫자까지 불러옴!
        rquser_data = qnum_list.filter(uid = user_info.id).count()
        
        #랭크 저장 코드
        #user_info.rank = rank_value
        #user_info.save()
        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestList
        fields= '__all__'
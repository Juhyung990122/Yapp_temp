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
        total = MgmtUser.objects.values('id').count()
        total_dic = {}
        for i in range(1,total+1):
            rquser_data = qnum_list.filter(uid = i).count()
            total_dic[i] = rquser_data
        total_dic = sorted(total_dic.items(), key = lambda x : x[1], reverse=True)
        
        
        #user_info.rank = total_list.index(user_info)
        #user_info.save()
        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestList
        fields= '__all__'
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
  
    def rank_save(self,user_info):
    rank_list = []
    #feed_count 갯수 기준으로 역순정렬
    for user in user_info:
        uid = user.id
        feed_count = len(Feed.objects.filter(uid=uid))
        rank_list.append([feed_count,uid])
    rank_list = sorted(rank_list, key = lambda x : -x[0])
    #feed_count를 rank값으로 변경 후 uid기준으로 순차정렬
    user_idx = 0
    for rank in range(1,len(rank_list)+1):
        rank_list[user_idx][0] = rank
        user_idx+=1
    rank_list = sorted(rank_list, key = lambda x : x[1])
    #uid별로 랭크값 갱신
    user_idx = 0
    for user in user_info:
        user.rank = rank_list[user_idx][0]   
        user_idx += 1
        user.save()
        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestList
        fields= '__all__'
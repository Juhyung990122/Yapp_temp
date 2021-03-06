from User.models import MgmtUser, Feed, QuestList
from rest_framework import serializers
from .models import QuestList
from rest_framework.fields import CurrentUserDefault

class UserjoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgmtUser
        fields = ['level','rank']

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
        #feed_count를 rank값으로 변경 후 uid기준으로 정렬 
        user_idx = 0
        for rank in range(1,len(rank_list)+1):
            rank_list[user_idx][0] = rank
            user_idx+=1
        rank_list = sorted(rank_list, key = lambda x : x[1])
        for i in rank_list:
            user = MgmtUser.objects.get(id = i[1])
            total = MgmtUser.objects.all().count()
            user.rank = round(i[0] / total * 100,1)
            user.save()
            
    def level_save(self,user_info):
        if user_info.experience >= 5:
            user_info.level += 1
            user_info.experience = 0
            user_info.save()

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserjoinSerializer(instance.uid).data
        return response

class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestList
        fields= '__all__'
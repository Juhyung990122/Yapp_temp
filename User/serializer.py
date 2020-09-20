from User.models import MgmtUser,Feed,QuestList
from rest_framework import serializers

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

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestList
        fields= '__all__'
from Ect.models import Trashcan,Token
from rest_framework import serializers

class TrashcanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trashcan
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
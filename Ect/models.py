from django.db import models
from User.models import User
from django.conf import settings

class Trashcan(models.Model):
    #MYSQL 에서는 Floatfield -> Double 데이터타입 생성
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    address = models.TextField()
    STATE = (
        ('C','confirmed'), 
        ('NC','notConfirmed')
    )
    state = models.CharField(max_length=15, choices=STATE, default='NC')

class Token(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    tokenString = models.TextField()
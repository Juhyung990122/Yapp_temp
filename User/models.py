from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib import auth
from django.conf import settings


class MgmtUser(AbstractUser):
    nickname = models.CharField(max_length = 100)
    level = models.IntegerField(default = 1)
    rank = models.FloatField(default = 0.0)
    registeredDate = models.DateTimeField(auto_now_add=True)  
    STATE = (
        ('N' , 'Normal'),
        ('D' , 'Dormant'),
        ('L', 'Leaved'),
    )  
    state = models.CharField(max_length=10, choices=STATE, default='N')

class Feed(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)  
    photo = models.ImageField()

class QuestList(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #qid = models.ForeignKey(Quest.Quest, on_delete = models.CASCADE))
    STATE = (
        ('TODO' , 'Normal'),
        ('DOING' , 'Dormant'),
        ('DONE', 'Leaved'),
    )
    state =  models.CharField(max_length=10, choices=STATE, default='TODO')
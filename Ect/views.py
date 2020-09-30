from django.shortcuts import render
from Ect.models import Trashcan,Token
from Ect.serializer import TrashcanSerializer, TokenSerializer
from rest_framework import viewsets
import json
import requests
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer

#라이브러리 사용시 삭제할 클래스.
class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

'''
프론트에서 푸시키오면 FCMDevice에 데이터 작성
@api_view(['POST'])
def push_notification_create():
    
'''
'''
mgmtuser.state가 D -> FCM server에 푸시알림 전송요청  
@api_view(['POST'])
def push_notification_request():
    #한사람 
    # device = FCMDevice.objects.get(registration_id=gcm_reg_id)
    #여러사람 
    #device = FCMDevice.objects.all()
    #device.send_message(title="Title", body="Message", data={"test": "test"})
'''
'''
라이브러리 미사용시 쓸 푸시알림기능
@api_view(['POST'])
def push_notification_create(mgmtuser의 uid):
    url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Authorization': 'key= <서버키 삽입>',
        'Content-Type': 'application/json; UTF-8',
    }
    content = {
        #보낼 대상지정
        'registration_ids': uid,
        'notification': {
            'title': 'test title',
            'body': 'test body'
        }
    }

    # json 파싱 후 requests 모듈로 FCM 서버에 요청
    requests.post(url, data=json.dumps(content), headers=headers)
'''
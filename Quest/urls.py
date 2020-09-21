from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Quest import views
from rest_framework import routers

quest_router = routers.DefaultRouter()
quest_router.register('',views.QuestViewSet)

urlpatterns = [
    path('quest/',include(quest_router.urls))
]
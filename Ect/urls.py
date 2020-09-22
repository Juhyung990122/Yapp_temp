from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Ect import views
from rest_framework import routers

trashcan_router = routers.DefaultRouter()
trashcan_router.register('',views.TrashcanViewSet)
token_router = routers.DefaultRouter()
token_router.register('',views.TokenViewSet)

urlpatterns = [
    path('trashcan/',include(trashcan_router.urls)),
    path('token/',include(token_router.urls))
]
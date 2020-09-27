from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from User import views
from rest_framework import routers

user_router = routers.DefaultRouter()
user_router.register('',views.MgmtUserViewSet)
feed_router = routers.DefaultRouter()
feed_router.register('',views.FeedViewSet)
questlist_router = routers.DefaultRouter()
questlist_router.register('',views.QuestListViewSet)

urlpatterns = [
    path('mgmtuser/',include(user_router.urls)),
    path('feed/',include(feed_router.urls)),
    path('questlist/',include(questlist_router.urls)),
    path('rank_update/<int:user_id>',views.calculate_rank)
]
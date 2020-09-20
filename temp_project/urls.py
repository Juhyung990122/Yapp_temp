from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from User import views
from rest_framework import routers

user_router = routers.DefaultRouter()
user_router.register('',views.MgmtUserViewSet)
feed_router = routers.DefaultRouter()
feed_router.register('',views.FeedViewSet)

urlpatterns = [
    path('yapptemp_admin/', admin.site.urls),
    path('mgmtuser/',include(user_router.urls)),
    path('feed/',include(feed_router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework'))
]

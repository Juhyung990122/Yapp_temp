from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('yapptemp_admin/', admin.site.urls),
    path('User/',include('User.urls')),
    path('Quest/',include('Quest.urls')),
    path('Planet/',include('Planet.urls')),
    path('Ect/',include('Ect.urls')),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework'))
]

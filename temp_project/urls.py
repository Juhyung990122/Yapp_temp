from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from django.conf import settings
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('yapptemp_admin/', admin.site.urls),
    path('User/',include('User.urls')),
    path('Quest/',include('Quest.urls')),
    path('Planet/',include('Planet.urls')),
    path('Ect/',include('Ect.urls')),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework'))
]

# 문서화 설정
# /swagger/로 접속
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'Job Query',
        default_version = 'v1',
        description = 'Search Tech Jobs',
    ),
    public = True,
    permission_classes = [permissions.AllowAny]
)

swagger_urlpatterns = [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('webscrawler.api.urls', 'info_api')),
]+swagger_urlpatterns

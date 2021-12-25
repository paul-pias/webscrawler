from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/info/', include('webscrawler.api.urls', 'info_api')),
]

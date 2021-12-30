from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from webscrawler.api.views import (
    initial_entry,
    bulk_entry,
    JobViewSet
    
)
app_name = "webscrawler"

urlpatterns = [
    path('initial-entry', initial_entry),
    path('bulk-entry', bulk_entry,),
    path('info/', JobViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('info/<int:pk>/',JobViewSet.as_view({
        'get': 'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy'
    }))
]
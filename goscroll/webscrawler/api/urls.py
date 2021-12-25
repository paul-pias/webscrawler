from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from webscrawler.api.views import (
    initial_entry,
)
app_name = "webscrawler"

urlpatterns = [
    path('initial-entry', initial_entry, name = 'initial_database_entry')

]
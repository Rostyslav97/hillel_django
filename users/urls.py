from django.urls import path
from django.urls.resolvers import URLPattern

from .views import users

urlpatterns = [
    path("users/", users)
]
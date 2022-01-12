from django.urls import path
from .views import users, SignUpView

urlpatterns = [
    path("users/", users),
    path("signup/", SignUpView.as_view(), name="signup"),
]
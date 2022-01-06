from django.urls import path

from .views import PostsView, PostDetailView

urlpatterns = [
    path("posts/", PostsView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view()),
]
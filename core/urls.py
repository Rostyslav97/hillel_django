from django.urls import path

from .views import PostsView, PostDetailView, PostCreateView

urlpatterns = [
    path("posts/", PostsView.as_view(), name = 'posts'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name = 'post'),
    path("post/create/", PostCreateView.as_view(), name='create'),
]
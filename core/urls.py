from django.urls import path

from .views import PostsView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path("posts_list/", PostsView.as_view(), name = 'posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name = 'post'),
    path("post/create/", PostCreateView.as_view(), name='create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='update'),
]
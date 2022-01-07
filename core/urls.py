from django.db.models.query import prefetch_related_objects
from django.urls import path

from .views import PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("posts/", PostsView.as_view(), name = 'posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name = 'post'),
    path("post/create/", PostCreateView.as_view(), name='create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
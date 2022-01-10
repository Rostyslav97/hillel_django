from django.urls import path
from .views import PostDeleteView, PostUpdateView, PostsView, PostDetailView, PostCreateView

app_name = "posts"

urlpatterns = [
    path("posts/", PostsView.as_view(), name ="list"),
    path("post_detail/<int:id>/", PostDetailView.as_view(), name="detail"),
    path("post_delete/<int:id>/", PostDeleteView.as_view(), name="delete"),
    path("post_update/<int:id>/", PostUpdateView.as_view(), name="update"),
    path("post_create/", PostCreateView.as_view(), name="create")

    # path("post/create/", PostCreateView.as_view(), name='create'),
    # path("post/<int:pk>/update/", PostUpdateView.as_view(), name='update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
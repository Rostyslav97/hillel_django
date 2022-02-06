from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

from .models import Post

from .forms import PostForm

# class PostsView(TemplateView):
#     template_name = "core/posts.html"

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all()
#         return ctx

User = get_user_model()

def get_user_posts(user: User) -> QuerySet:
    if not isinstance(user, User):
            raise ValueError("Please login")

    qs = Post.objects.filter(user=user)
    return qs


class PostsView(ListView):
    template_name = "core/posts.html"
    context_object_name = "posts"
    # queryset = Post.objects.all()

    def get_queryset(self):
        return get_user_posts(self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        results = [
            (
                p, 
                p.like_set.filter(status=True).count(), 
                p.like_set.filter(status=False).count()
            ) 
            for p in posts
        ]
        ctx['results'] = results
        return ctx


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'core/post.html' 
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return get_user_posts(self.request.user)

class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'core/post_delete.html'
    pk_url_kwarg = 'id'
    # success_url = '/posts/'
    success_url = reverse_lazy("posts:list")

    def get_queryset(self):
        return get_user_posts(self.request.user)


class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'core/post_update.html'
    pk_url_kwarg = 'id'
    fields = ['title', 'content']
    success_url = reverse_lazy("posts:list")

    def get_queryset(self):
        return get_user_posts(self.request.user)
    

class PostCreateView(CreateView):
    queryset = Post.objects.all()
    template_name = 'core/post_create.html'
    # fields = ['title', 'content', 'user'] ---> can be used only with model, when there is no form
    form_class = PostForm
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'core/create.html'
#     fields = ['title', 'content', 'image', 'user']

# class PostUpdateView(UpdateView):
#     model = Post
#     template_name = 'core/update.html'
#     fields = ['title', 'content', 'image']

# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'core/delete.html'
#     success_url = reverse_lazy('posts')
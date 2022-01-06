from django.views.generic import ListView, DetailView, CreateView
from .models import Like, Post


# class PostsView(TemplateView):
#     template_name = "core/posts.html"

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all()
#         return ctx

class PostsView(ListView):
    template_name = "core/posts.html"
    queryset = Post.objects.all()
#   context_object_name = "posts"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
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

class PostCreateView(CreateView):
    model = Post
    template_name = 'core/create.html'
    fields = ['title', 'content', 'image', 'user']
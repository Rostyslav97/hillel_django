from django.http.response import HttpResponse
from django.views.generic import ListView
from .models import Post


# class PostsView(TemplateView):
#     template_name = "core/posts.html"

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all()
#         return ctx

class PostsView(ListView):
    template_name = "core/posts.html"
    queryset = Post.objects.all()

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class HomeView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'blog/home.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug'))


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'





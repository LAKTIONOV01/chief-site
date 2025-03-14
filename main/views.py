from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug'))


def home(request):
    return render(request, 'base.html')

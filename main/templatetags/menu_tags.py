from django import template
from ..models import Categories, Post

register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    categories = Categories.objects.all()
    return {'categories': categories}


@register.inclusion_tag('blog/include/tags/posts_menu.html')
def get_last_posts():
    posts = Post.objects.order_by('-id')[:5]
    return {'last_posts': posts}

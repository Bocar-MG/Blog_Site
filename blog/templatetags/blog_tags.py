from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe
from ..models import Post
from django import template

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-date_publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag(name='most_commented_posts')
def show_most_commented_posts(count=5):
    most_commented_posts = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return most_commented_posts


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

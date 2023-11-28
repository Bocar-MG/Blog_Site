from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog.models import Post


# Create your views here.

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'dashboard/dashboard.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__id=user.id)


class PostCreateView(CreateView):
    model = Post
    template_name = "dashboard/new_post.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:dashboard')


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = "dashboard/update_post.html"
    fields = ["title","body"]

    def form_valid(self, form):
        form.instance.slug=slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:dashboard')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "dashboard/delete_post.html"
    success_url = reverse_lazy("dashboard:dashboard")



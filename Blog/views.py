from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from Blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy("Blog:all")


class PostDetailView(DetailView):
    model = Post



class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")

    

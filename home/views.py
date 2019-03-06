from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects
    return render(request, 'home/home.html', {'posts': posts})


def detail(request, post_id):
    detailpost = get_object_or_404(Post, pk=post_id)
    return render(request, 'home/detail.html', {'post': detailpost})

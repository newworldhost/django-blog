from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    Models = Post
    queryset = Post.objects.all()
    #template post_list.html



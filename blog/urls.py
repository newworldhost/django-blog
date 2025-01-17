from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views




urlpatterns = [
    path('blog', include("blog.urls"), name="blog-urls"),
    path('', views.PostList.as_view(), name='home'),
]
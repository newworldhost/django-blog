from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("<int:event_id>/", views.event_detail, name="event_detail") 
]

from django.urls import path
from . import views
urlpatterns = [
    path("", views.landing , name="landing" ) ,
    path("posts", views.posts , name="posts" ) ,
    path("post", views.post , name="post" ) ,
    path("video_post", views.video_post , name="video_post" ) ,
]

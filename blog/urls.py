from django.urls import path
from . import views
urlpatterns = [
    path("", views.landing , name="landing" ) ,
    path("posts/<str:category>/", views.posts , name="posts" ) ,
    path("post/<str:title>/", views.post , name="post" ) ,
    path("search/", views.search , name="search" ) ,
    path("last_posts/",views.last_posts,name="last_posts"),
]

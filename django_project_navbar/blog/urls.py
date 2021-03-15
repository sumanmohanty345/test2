
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView)
from django.urls import path
from . import views




urlpatterns=[
    # path('',views.home,name="blog_home"),
    path('user/<str:username>',UserPostListView.as_view(),name='user_posts'),

    path('',PostListView.as_view(),name='blog_home'),

    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),

    path('post/new/',PostCreateView.as_view(),name='post_create'),

    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),

    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),

    path('about/',views.about,name="blog_about"),

    path('blog_python/',views.blog_python_view,name="blog_python"),

    path('latest-posts/',views.LatestListView, name='latest_posts'),

    path('top-questions/',views.top_questions, name='top_questions'),



]

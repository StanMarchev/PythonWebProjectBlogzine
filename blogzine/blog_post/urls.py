from django.urls import path, include

from blogzine.blog_post.views import PostCreateView, PostEditView, post_list, PostDetailView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('post-list/', post_list, name='post-list'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
]
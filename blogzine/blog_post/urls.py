from django.urls import path, include

from blogzine.blog_post.views import PostDetailsView, PostCreateView, PostEditView, post_list

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('post-list/', post_list, name='post-list'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
]